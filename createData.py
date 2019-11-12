import jieba
import codecs 

disease_list = []
Question_list = []
Type_list = []
'''
with codecs.open('disease.txt',encoding='utf-8') as infile:
   

    for line in infile:
        if line[:-5] not in disease_list:
            disease_list.append(line[:-5])
infile.close()
''''
with codecs.open('Q.txt', encoding='utf-8') as infile:
    for line in infile:
        if line[:-1] not in Question_list:
            Question_list.append(lien[:-1])
infile.close()

print(Question_list)