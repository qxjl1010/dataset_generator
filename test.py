import jieba
import codecs 
import datetime
import random
import numpy

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline

disease_list = []
symptom_list = []
Question_list = []
L_Question_list = []
Type_list = []
L_Type_list = []

jieba.load_userdict("dictionary.txt")


# 训练模型
def train_model():

	with codecs.open('disease.txt',encoding='utf-8') as infile:

		i = 0
		for line in infile:
			if i == 0:
				disease_list.append(line[1:-3])
				i += 1
				continue
			if line[:-3] not in disease_list:
				disease_list.append(line[:-3])
	infile.close()
	with codecs.open('symptoms.txt',encoding='utf-8') as infile:

		i = 0
		for line in infile:
			if i == 0:
				symptom_list.append(line[1:-3])
				i += 1
				continue
			if line[:-3] not in symptom_list:
				symptom_list.append(line[:-3])
	infile.close()
	print(symptom_list)


	with codecs.open('Q.txt', encoding='utf-8') as infile:
		i = 0
		for line in infile:
			if i == 0:
				i += 1
				continue
			elif i == 1:
				line = line.replace('偏头痛','XXX')
				Question_list.append(line[:-3])
				i += 1
				continue
			line = line.replace('偏头痛','XXX')
			if line[:-2] not in Question_list:
				Question_list.append(line[:-2])
			else:
				print(line)
	infile.close()

	with open('T.txt') as infile:
		for line in infile:
			Type_list.append(int(line[:-1]))
	infile.close()

	for i in range(1):
		for line,type in zip(Question_list,Type_list):
			# seg = line.replace('XXX',disease_list[i])
			
			seg_list = jieba.lcut(line, cut_all=False)
			q_addSpace = ''
			for w in seg_list:
				q_addSpace = q_addSpace + w + ' '
			L_Question_list.append(q_addSpace[:-1])
			L_Type_list.append(type)

	li=list(range(len(L_Question_list)))
	random.shuffle(li)  

	shuffled_L_Question_list = [x for _,x in sorted(zip(li,L_Question_list))]
	shuffled_L_Type_list = [x for _,x in sorted(zip(li,L_Type_list))]

	model = Pipeline([('vect', TfidfVectorizer()), ('tfidf', TfidfTransformer()), ('clf', SVC(C=0.99, kernel = 'linear', probability=True))])
	model = model.fit(shuffled_L_Question_list, shuffled_L_Type_list)
	return model

def find_disease( q):
	for i in range(len(q)):
		for j in range(len(q) - i):
			if q[i:len(q)-j] in disease_list:
				print(q[i:len(q)-j])
				thisDisease = q[i:len(q)-j]
				q = q.replace(q[i:len(q)-j], 'XXX')
				return q, thisDisease

	return q, 'null'

def find_symptom(q):
	thisSymptom = []
	for i in range(len(q)):
		for j in range(len(q) - i):
			if q[i:len(q)-j] in symptom_list:
				thisSymptom.append(q[i:len(q)-j])
				q = q.replace(q[i:len(q)-j], 'XXX')
				return q, thisSymptom

	return q, thisSymptom

def cut_sentence(q):
	print(q)
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

def answering(model, q):
	thisIntent = []
	q,thisDisease = find_disease(q)
	q,thisSymptoms = find_symptom(q)
	if thisSymptoms != [] and thisDisease == 'null':
		print('enter 1')
		thisIntent.append('symptom_diagnose')

	ph, intent_ph = cut_sentence(q)
	print(ph)
	print(intent_ph)
	for p in ph:
		print(p)
		seg_list = jieba.lcut(p, cut_all=False)
		p_addSpace = ''
		for w in seg_list:
			p_addSpace = p_addSpace + w + ' '
		predicted = model.predict([p_addSpace[:-1]])
		pred_prob = model.predict_proba([p_addSpace[:-1]])
		print('predict:')
		print(predicted[0])
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
			thisIntent.append('symptom_diagnose')
	
	for p in intent_ph:
		seg_list = jieba.lcut(p, cut_all=False)
		p_addSpace = ''
		for w in seg_list:
			p_addSpace = p_addSpace + w + ' '
		predicted = model.predict([p_addSpace[:-1]])
		pred_prob = model.predict_proba([p_addSpace[:-1]])
		print('predict:')
		print(predicted[0])
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
    rst = answering(text_clf, q)
    print(rst)
