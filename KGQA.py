import jieba
import codecs 
import datetime
import random
import numpy

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline

# logic for Symptom
# 1. Symptom must go to Disease
# 2. Cut by punctuation
# 3. Question Mark must be intent
# 4. Last part must be intent


class KGQA1():

    # 训练模型
    def __init__(self):
        self.disease_list = []
        self.symptom_list = []
        self.Question_list = []
        self.L_Question_list = []
        self.Type_list = []
        self.L_Type_list = []
        with codecs.open('./kgqa/disease.txt',encoding='utf-8') as infile:
   
            i = 0
            for line in infile:
                if i == 0:
                    self.disease_list.append(line[1:-5])
                    i += 1
                    continue
                if line[:-5] not in self.disease_list:
                    self.disease_list.append(line[:-5])
        infile.close()

        with codecs.open('./kgqa/symptoms.txt',encoding='utf-8') as infile:
   
            i = 0
            for line in infile:
                if i == 0:
                    self.symptom_list.append(line[1:-5])
                    i += 1
                    continue
                if line[:-5] not in self.symptom_list:
                    self.symptom_list.append(line[:-5])
        infile.close()


        with codecs.open('./kgqa/Q.txt', encoding='utf-8') as infile:
            i = 0
            for line in infile:
                if i == 0:
                    i += 1
                    continue
                elif i == 1:
                    line = line.replace('偏头痛','XXX')
                    self.Question_list.append(line[:-3])
                    i += 1
                    continue
                line = line.replace('偏头痛','XXX')
                if line[:-2] not in self.Question_list:
                    self.Question_list.append(line[:-2])
                else:
                    print(line)
        infile.close()

        with open('./kgqa/T.txt') as infile:
            for line in infile:
                self.Type_list.append(int(line[:-1]))
        infile.close()
        jieba.load_userdict("./kgqa/dictionary.txt")

        for i in range(1):
            for line,type in zip(self.Question_list,self.Type_list):
                # seg = line.replace('XXX',self.disease_list[i])
                
                seg_list = jieba.lcut(line, cut_all=False)
                q_addSpace = ''
                for w in seg_list:
                    q_addSpace = q_addSpace + w + ' '
                self.L_Question_list.append(q_addSpace[:-1])
                self.L_Type_list.append(type)

        li=list(range(len(self.L_Question_list)))
        random.shuffle(li)  

        shuffled_L_Question_list = [x for _,x in sorted(zip(li,self.L_Question_list))]
        shuffled_L_Type_list = [x for _,x in sorted(zip(li,self.L_Type_list))]

        model = Pipeline([('vect', TfidfVectorizer()), ('tfidf', TfidfTransformer()), ('clf', SVC(C=0.99, kernel = 'linear', probability=True))])
        model = model.fit(shuffled_L_Question_list, shuffled_L_Type_list)
        self.model = model
    # Need change logic for multiple diseases
    def find_disease(self, q):
        for i in range(len(q)):
            for j in range(len(q) - i):
                if q[i:len(q)-j] in self.disease_list:
                    thisDisease = q[i:len(q)-j]
                    q = q.replace(q[i:len(q)-j], 'XXX')
                    return q, thisDisease
    
        return q, 'null'
    
    def find_symptom(self,q):
        thisSymptom = []
        for i in range(len(q)):
            for j in range(len(q) - i):
                if q[i:len(q)-j] in self.symptom_list:
                    thisSymptom.append(q[i:len(q)-j])
                    q = q.replace(q[i:len(q)-j], 'XXX')
                    return q, thisSymptom
    
        return q, thisSymptom

    def cut_sentence(self,q):
        phrase = []
        intent_phrase = []
        cut_point = [0]
        question_mark = []
        pos = 0
        for i in q:
            if i == '。':
                cut_point.append(pos)
            elif i == '？':
                cut_point.append(pos)
                question_mark.append(pos)
            pos += 1
        for i in range(len(cut_point)-1):
            sentence = q[int(cut_point[i]): int(cut_point[i+1]+1)]
            if cut_point[i+1] in question_mark:
                intent_phrase.append(sentence)
            else:
                phrase.append(sentence)
        if phrase == [] and intent_phrase == []:
            phrase.append(q)
        return phrase, intent_phrase

    def answering(self, q):
        thisIntent = []
        q,thisDisease = self.find_disease(q)
        q,thisSymptoms = self.find_symptom(q)
        if thisSymptoms != [] and thisDisease == 'null':
            thisIntent.append('symptom_diagnose')

        ph, intent_ph = self.cut_sentence(q)
        
        for p in ph:

            seg_list = jieba.lcut(p, cut_all=False)
            p_addSpace = ''
            for w in seg_list:
                p_addSpace = p_addSpace + w + ' '
            predicted = self.model.predict([p_addSpace[:-1]])
            pred_prob = self.model.predict_proba([p_addSpace[:-1]])
        
            if predicted[0] == 1:
                thisIntent.append('disease_treatment')
            elif predicted[0] == 2:
                thisIntent.append('disease_examination')
            elif predicted[0] == 3:
                thisIntent.append('disease_medicine')
            elif predicted[0] == 4:
                thisIntent.append('disease_symptom')
            elif predicted[0] == 5:
                thisIntent.append('disease_cause')
            elif predicted[0] == 6:
                thisIntent.append('disease_associated')
            elif predicted[0] == 7:
                thisIntent.append('disease_tendency')
            elif predicted[0] == 8:
                thisIntent.append('disease_bodyParts')
        
        for p in intent_ph:
            seg_list = jieba.lcut(p, cut_all=False)
            p_addSpace = ''
            for w in seg_list:
                p_addSpace = p_addSpace + w + ' '
            predicted = self.model.predict([p_addSpace[:-1]])
            pred_prob = self.model.predict_proba([p_addSpace[:-1]])
        
            if predicted[0] == 1:
                thisIntent.append('disease_treatment')
            elif predicted[0] == 2:
                thisIntent.append('disease_examination')
            elif predicted[0] == 3:
                thisIntent.append('disease_medicine')
            elif predicted[0] == 4:
                thisIntent.append('disease_symptom')
            elif predicted[0] == 5:
                thisIntent.append('disease_cause')
            elif predicted[0] == 6:
                thisIntent.append('disease_associated')
            elif predicted[0] == 7:
                thisIntent.append('disease_tendency')
            elif predicted[0] == 8:
                thisIntent.append('disease_bodyParts')


        thisMedicines = []
        return_diseases = [thisDisease]
        

        result = {"diseases": return_diseases, "symptoms": thisSymptoms, "medicines": thisMedicines, "intent": thisIntent}
        return result

text_clf = train_model()
while True:
    q = input('请输入您的问题: ')
    d,i = answering(text_clf, q)
    print(d)
    print(i)