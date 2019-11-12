# Import BinaryRelevance from skmultilearn
from skmultilearn.problem_transform import BinaryRelevance

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import SVC
from scipy import sparse 
import jieba
import codecs
import numpy as np

from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)


class KGQA2():

    def __init__(self):
        self.Q_list = []
        self.L_list = []
        self.L_Question_list = []
        self.disease_list = []
        self.symptom_list = []

        with codecs.open('./kgqa2/disease.txt',encoding='utf-8') as infile:
   
            i = 0
            for line in infile:
                if i == 0:
                    self.disease_list.append(line[1:-5])
                    i += 1
                    continue
                if line[:-5] not in self.disease_list:
                    self.disease_list.append(line[:-5])
        infile.close()

        with codecs.open('./kgqa2/symptoms.txt',encoding='utf-8') as infile:
   
            i = 0
            for line in infile:
                if i == 0:
                    self.symptom_list.append(line[1:-5])
                    i += 1
                    continue
                if line[:-5] not in self.symptom_list:
                    self.symptom_list.append(line[:-5])
        infile.close()


        # Read Sentence file
        with codecs.open('./kgqa2/multi-label-Q.txt',encoding='utf-8') as infile:
            for line in infile:
                self.Q_list.append(line[:-2])
        infile.close()

        # Read Label file
        with open('./kgqa2/multi-label-L.txt') as infile:
            for line in infile:
                tmp_l = line[:-1].split(',')
                self.L_list.append(tmp_l)
        infile.close()

        self.L_list = np.array(self.L_list)

        # Preprocess for Chinese sentences
        for line in self.Q_list:
            seg_list = jieba.lcut(line, cut_all=False)
            q_addSpace = ''
            for w in seg_list:
                q_addSpace = q_addSpace + w + ' '
            self.L_Question_list.append(q_addSpace[:-1])

        self.cv = CountVectorizer()
        self.cv_fit=self.cv.fit_transform(self.L_Question_list)

        self.transformer = TfidfTransformer()
        self.tfidf = self.transformer.fit_transform(self.cv_fit)

        self.M = sparse.lil_matrix((len(self.L_list),6), dtype=int)
        for i,row in enumerate(self.L_list):
            count = 0
            for col in row:
                self.M[i, count] = col
                count += 1

        # Setup the classifier
        self.clf = BinaryRelevance(classifier=SVC())

        # Train
        self.clf.fit(self.tfidf, self.M)
    
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
        # Preprocess for Chinese sentence
        seg_list = jieba.lcut(q, cut_all=False)
        q_addSpace = ''
        for w in seg_list:
            q_addSpace = q_addSpace + w + ' '
        return [q_addSpace]


    def answering(self,q):
        # A sentence in train dataset
        # x_test = '孩子发烧39度咽喉肿痛咳黄痰怎么办？退烧后持续咳嗽需要换药吗？'
        q, thisDisease = self.find_disease(q)
        q, thisSymptoms = self.find_symptom(q)
        X_test = self.cut_sentence(q)
        cv_fit2= self.cv.transform(X_test)
        tfidf2 = self.transformer.transform(cv_fit2)

        # Predict
        pred = self.clf.predict(tfidf2)

        return_diseases = [thisDisease]
        return {"diseases": return_diseases, "symptoms": thisSymptoms, 'intent': pred.todense().getA().tolist()}
