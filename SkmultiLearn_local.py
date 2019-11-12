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




Q_list = []
L_list = []
L_Question_list = []
disease_list = []
symptom_list = []
# Read Sentence file
with codecs.open('multi-label-Q.txt',encoding='utf-8') as infile:
	for line in infile:
		Q_list.append(line[:-2])
infile.close()

with codecs.open('disease.txt',encoding='utf-8') as infile:

	i = 0
	for line in infile:
		if i == 0:
			disease_list.append(line[1:-5])
			i += 1
			continue
		if line[:-5] not in disease_list:
			disease_list.append(line[:-5])
infile.close()

with codecs.open('symptoms.txt',encoding='utf-8') as infile:

	i = 0
	for line in infile:
		if i == 0:
			symptom_list.append(line[1:-5])
			i += 1
			continue
		if line[:-5] not in symptom_list:
			symptom_list.append(line[:-5])
infile.close()



# Read Label file
with open('multi-label-L.txt') as infile:
	for line in infile:
		tmp_l = line[:-1].split(',')
		L_list.append(tmp_l)
infile.close()

L_list = np.array(L_list)

# Preprocess for Chinese sentences
for line in Q_list:
	seg_list = jieba.lcut(line, cut_all=False)
	q_addSpace = ''
	for w in seg_list:
		q_addSpace = q_addSpace + w + ' '
	L_Question_list.append(q_addSpace[:-1])

cv = CountVectorizer()
cv_fit=cv.fit_transform(L_Question_list)

transformer = TfidfTransformer()
tfidf = transformer.fit_transform(cv_fit)

M = sparse.lil_matrix((len(L_list),6), dtype=int)
for i,row in enumerate(L_list):
	count = 0
	for col in row:
		M[i, count] = col
		count += 1

# Setup the classifier
clf = BinaryRelevance(classifier=SVC())

# Train
clf.fit(tfidf, M)

def find_symptom(q):
	thisSymptom = []
	for i in range(len(q)):
		for j in range(len(q) - i):
			if q[i:len(q)-j] in symptom_list:
				thisSymptom.append(q[i:len(q)-j])
				q = q.replace(q[i:len(q)-j], 'XXX')
				return q, thisSymptom

	return q, thisSymptom

def find_disease(q):
	for i in range(len(q)):
		for j in range(len(q) - i):
			if q[i:len(q)-j] in disease_list:
				thisDisease = q[i:len(q)-j]
				q = q.replace(q[i:len(q)-j], 'XXX')
				return q, thisDisease

	return q, 'null'

def cut_sentence(q):
	# Preprocess for Chinese sentence
	seg_list = jieba.lcut(q, cut_all=False)
	q_addSpace = ''
	for w in seg_list:
		q_addSpace = q_addSpace + w + ' '
	return [q_addSpace]



# A sentence in train dataset
x_test = '孩子发烧39度咽喉肿痛中度贫血怎么办？退烧后持续咳嗽需要换药吗？'
q, thisDisease = find_disease(x_test)
q, thisSymptoms = find_symptom(q)

X_test = cut_sentence(q)
cv_fit2= cv.transform(X_test)
tfidf2 = transformer.transform(cv_fit2)

# Predict
pred = clf.predict(tfidf2)
return_diseases = [thisDisease]
print({"diseases": return_diseases, "symptoms": thisSymptoms, 'intent': pred.todense().getA().tolist()})

