disease_list = []
symptom_list = []
drug_list = []

def find_entity(q):
    show_dict = {'get question:':q}
    print('=======================================================')
    print('question get:')
    print(q)
    print('-------------------------------------------------------')
    with open('disease.txt', 'r', encoding='utf-8') as infile:
   
        i = 0
        for line in infile:
            if i == 0:
                disease_list.append(line[1:-2])
                i += 1
                continue
            if line[:-4] not in disease_list:
                disease_list.append(line[:-2])
    infile.close()

    with open('symptoms.txt', 'r', encoding='utf-8') as infile:
   
        i = 0
        for line in infile:
            if i == 0:
                symptom_list.append(line[1:-2])
                i += 1
                continue
            if line[:-4] not in symptom_list:
                symptom_list.append(line[:-2])
    infile.close()

    with open('drug.txt', 'r', encoding='utf-8') as infile:
   
        i = 0
        for line in infile:
            if len(line) <= 1:
                continue
            if i == 0:
                drug_list.append(line[1:-1])
                i += 1
                continue
            if line[:-1] not in drug_list:
                drug_list.append(line[:-1])
    infile.close()
    print('LEN!!!!!!!!!!')
    print(len(drug_list))
    thisSymptom = []
    thisDisease = []
    thisDrug = []
    for i in range(len(q)):
        for j in range(len(q) - i):
           if q[i:len(q)-j] in drug_list:
                print('APPEND!!!!!!')
                print(q[i:len(q)-j])
                thisDrug.append(q[i:len(q)-j])
                q = q.replace(q[i:len(q)-j], 'MED')

    for i in range(len(q)):
        for j in range(len(q) - i):
           if q[i:len(q)-j] in disease_list:
                thisDisease.append(q[i:len(q)-j])
                q = q.replace(q[i:len(q)-j], 'DIS')

    show_dict['get_diease'] = thisDisease
    '''
    print('after diseases searching, get disease(s):')
    print(thisDisease)
    print('question change to:')
    print(q)
    print('-------------------------------------------------------')
    '''
    for i in range(len(q)):
        for j in range(len(q) - i):
           if q[i:len(q)-j] in symptom_list:
                
                thisSymptom.append(q[i:len(q)-j])
                q = q.replace(q[i:len(q)-j], 'SPT')
                # return q, thisSymptom
    show_dict['get_symptom:'] = thisSymptom
    '''
    print('after symptoms searching, get symptoms(s):')
    print(thisSymptom)
    print('question change to:')
    print(q)
    print('-------------------------------------------------------')       
    '''
    # return q, thisSymptom

    return q, thisSymptom, thisDisease, thisDrug, show_dict
sentence_str ='儿童可以吃异物巴比妥吗？我外公，80岁，昨天扭了腰，今天上午，在床上，表面图形觉倒错，记忆错误，顽固性头痛，怎么回事？下颌下腺炎症要去哪里看？'

q, s, d, dg, dict = find_entity(sentence_str)

return_dict = {'疾病:':d, '症状:':s, '药品':dg,'意图:':'null'}

dict['疾病'] = d
dict['症状'] = s
dict['意图'] = 'null'
print(q)
print(return_dict)



with open('collect_data.txt','a', encoding='utf-8') as infile:
    infile.write(q)