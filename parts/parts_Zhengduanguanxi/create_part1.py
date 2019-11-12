import random

sra_list = []
jh_list = []
did_list = []
tl_list = []
label_1_l = []

jh_0_5_list = []
jh_5_25_list = []
jh_25_55_list = []
jh_55_80_list = []

sra_0_5_list = []
sra_5_25_list = []
sra_25_55_list = []
sra_55_80_list = []

step_1_list = []
step_2_list = []
step_3_list = []
step_4_list = []
step_5_list = []

with open('sex_relation+age.txt', encoding='utf-8') as infile:
    i = 0
    for line in infile:
        if i == 0:
            sra_list.append(line[1:-1])
            if '(0-5)' in line:
                sra_0_5_list.append(line[1:-1])
            elif '(5-25)' in line:
                sra_5_25_list.append(line[1:-1])
            elif '(25-55)' in line:
                sra_25_55_list.append(line[1:-1])
            elif '(55-80)' in line:
                sra_55_80_list.append(line[1:-1])
            i += 1
        else:
            sra_list.append(line[:-1])
            if '(0-5)' in line:
                sra_0_5_list.append(line[:-1])
            elif '(5-25)' in line:
                sra_5_25_list.append(line[:-1])
            elif '(25-55)' in line:
                sra_25_55_list.append(line[:-1])
            elif '(55-80)' in line:
                sra_55_80_list.append(line[:-1])
infile.close()

with open('job+history.txt', encoding='utf-8') as infile:
    i = 0
    for line in infile:
        if i == 0:
            jh_list.append(line[1:-1])
            if '(0-5)' in line:
                jh_0_5_list.append(line[1:-1])
            elif '(5-25)' in line:
                jh_5_25_list.append(line[1:-1])
            elif '(25-55)' in line:
                jh_25_55_list.append(line[1:-1])
            elif '(55-80)' in line:
                jh_55_80_list.append(line[1:-1])
            i += 1
        else:
            jh_list.append(line[:-1])
            if '(0-5)' in line:
                jh_0_5_list.append(line[:-1])
            elif '(5-25)' in line:
                jh_5_25_list.append(line[:-1])
            elif '(25-55)' in line:
                jh_25_55_list.append(line[:-1])
            elif '(55-80)' in line:
                jh_55_80_list.append(line[:-1])
infile.close()

with open('did.txt', encoding='utf-8') as infile:
    i = 0
    for line in infile:
        if i == 0:
            did_list.append(line[1:-1])
            i += 1
        else:
            did_list.append(line[:-1])
infile.close()

with open('time+location.txt', encoding='utf-8') as infile:
    i = 0
    for line in infile:
        if i == 0:
            tl_list.append(line[1:-1])
            i += 1
        else:
            tl_list.append(line[:-1])
infile.close()


with open('label_1_q.txt', encoding='utf-8') as infile:
    i = 0
    for line in infile:
        if i == 0:
            label_1_l.append(line[1:-1])
            i += 1
        else:
            label_1_l.append(line[:-1])
infile.close()

for i in range(100):
    STP_num = random.randint(1,3)
    STP_part = ''
    for i in range(STP_num):
        STP_part += 'STP，'
    step_1_list.append(STP_part + label_1_l[random.randint(0,len(label_1_l)-1)])

for i in range(len(step_1_list)):
    rd = random.randint(1,10)
    if rd > 8:
        step_2_list.append(tl_list[random.randint(0,len(tl_list)-1)] + '，' + step_1_list[i])
    else:
        step_2_list.append(step_1_list[i])

for i in range(len(step_2_list)):
    rd = random.randint(1,10)
    if rd > 8:
        step_3_list.append(did_list[random.randint(0,len(did_list)-1)] + '，' + step_2_list[i])
    else:
        step_3_list.append(step_2_list[i])


for i in range(len(step_3_list)):
    rd = random.randint(1,10)
    if rd > 8:
        if '(5-25)' in step_3_list[i]:
            step_4_list.append(jh_5_25_list[random.randint(0,len(jh_5_25_list)-1)] + '，' + step_3_list[i][6:])
        elif '(25-55)' in step_3_list[i]:
            step_4_list.append(jh_25_55_list[random.randint(0,len(jh_25_55_list)-1)] + '，' + step_3_list[i][7:])
        elif '(55-80)' in step_3_list[i]:
            step_4_list.append(jh_55_80_list[random.randint(0,len(jh_55_80_list)-1)] + '，' + step_3_list[i][7:])
        else:
            step_4_list.append(jh_list[random.randint(0,len(jh_list)-1)] + '，' + step_3_list[i])
    else:
        step_4_list.append(step_3_list[i])


for i in range(len(step_4_list)):
    rd = random.randint(1,10)
    if rd > 5:
        if '(0-5)' in step_4_list[i]:
            step_5_list.append(sra_0_5_list[random.randint(0,len(sra_0_5_list)-1)][5:] + '，' + step_4_list[i][5:])
        if '(5-25)' in step_4_list[i]:
            step_5_list.append(sra_5_25_list[random.randint(0,len(sra_5_25_list)-1)][6:] + '，' + step_4_list[i][6:])
        elif '(25-55)' in step_4_list[i]:
            step_5_list.append(sra_25_55_list[random.randint(0,len(sra_25_55_list)-1)][7:] + '，' + step_4_list[i][7:])
        elif '(55-80)' in step_4_list[i]:
            step_5_list.append(sra_55_80_list[random.randint(0,len(sra_55_80_list)-1)][7:] + '，' + step_4_list[i][7:])
        else:
            rd = random.randint(0,len(sra_list)-1)
            s = sra_list[rd][sra_list[rd].index(')')+1:]
            step_5_list.append(s + '，' + step_4_list[i])
    else:
        step_5_list.append(step_4_list[i])

for i in range(len(step_5_list)):
    if ')' in step_5_list[i]:
        step_5_list[i] = step_5_list[i][step_5_list[i].index(')')+1:]

print(step_5_list)