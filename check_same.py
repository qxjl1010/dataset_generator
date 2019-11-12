import codecs

disease_list = []
symptom_list = []

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

with codecs.open('症状.txt',encoding='utf-8') as infile:

    i = 0
    for line in infile:
        if i == 0:
            symptom_list.append(line[1:-5])
            i += 1
            continue
        if line[:-5] not in symptom_list:
            symptom_list.append(line[:-5])
infile.close()

s1 = set(disease_list)
s2 = set(symptom_list)

print(s1 & s2)