# -*- coding: UTF-8 -*-
import random

def create_labelZhengduanguanxi_list():
    sra_list = []
    hw_list = []
    jh_list = []
    did_list = []
    tl_list = []
    label_1_l = []

    jh_0_5_list = []
    jh_5_25_list = []
    jh_25_55_list = []
    jh_55_80_list = []

    hw_0_5_list = []
    hw_5_25_list = []
    hw_25_55_list = []
    hw_55_80_list = []

    sra_0_5_list = []
    sra_5_25_list = []
    sra_25_55_list = []
    sra_55_80_list = []

    add_tl_step = []
    add_did_step = []
    add_jh_step = []
    add_hw_step = []
    add_sra_step = []
    clean_step = []


    with open('parts/parts_Zhengduanguanxi/sex_relation+age.txt', encoding='utf-8') as infile:
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

    with open('parts/parts_Zhengduanguanxi/height+weight.txt', encoding='utf-8') as infile:
        i = 0
        for line in infile:
            if i == 0:
                hw_list.append(line[1:-1])
                if '(0-5)' in line:
                    hw_0_5_list.append(line[1:-1])
                elif '(5-25)' in line:
                    hw_5_25_list.append(line[1:-1])
                elif '(25-55)' in line:
                    hw_25_55_list.append(line[1:-1])
                elif '(55-80)' in line:
                    hw_55_80_list.append(line[1:-1])
                i += 1
            else:
                hw_list.append(line[:-1])
                if '(0-5)' in line:
                    hw_0_5_list.append(line[:-1])
                elif '(5-25)' in line:
                    hw_5_25_list.append(line[:-1])
                elif '(25-55)' in line:
                    hw_25_55_list.append(line[:-1])
                elif '(55-80)' in line:
                    hw_55_80_list.append(line[:-1])
    infile.close()


    with open('parts/parts_Zhengduanguanxi/job+history.txt', encoding='utf-8') as infile:
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
                if '(5-25)' in line:
                    jh_5_25_list.append(line[:-1])
                elif '(25-55)' in line:
                    jh_25_55_list.append(line[:-1])
                elif '(55-80)' in line:
                    jh_55_80_list.append(line[:-1])
    infile.close()

    with open('parts/parts_Zhengduanguanxi/did.txt', encoding='utf-8') as infile:
        i = 0
        for line in infile:
            if i == 0:
                did_list.append(line[1:-1])
                i += 1
            else:
                did_list.append(line[:-1])
    infile.close()

    with open('parts/parts_Zhengduanguanxi/time+location.txt', encoding='utf-8') as infile:
        i = 0
        for line in infile:
            if i == 0:
                tl_list.append(line[1:-1])
                i += 1
            else:
                tl_list.append(line[:-1])
    infile.close()


    with open('parts/parts_Zhengduanguanxi/label_1_q.txt', encoding='utf-8') as infile:
        i = 0
        for line in infile:
            if i == 0:
                label_1_l.append(line[1:-1])
                i += 1
            else:
                label_1_l.append(line[:-1])
    infile.close()

    for i in range(200):
        STP_num = random.randint(1,3)
        STP_part = ''
        for i in range(STP_num):
            STP_part += 'STP，'
        add_tl_step.append(STP_part + label_1_l[random.randint(0,len(label_1_l)-1)])

    for i in range(len(add_tl_step)):
        rd = random.randint(1,10)
        if rd > 8:
            add_did_step.append(tl_list[random.randint(0,len(tl_list)-1)] + '，' + add_tl_step[i])
        else:
            add_did_step.append(add_tl_step[i])

    for i in range(len(add_did_step)):
        rd = random.randint(1,10)
        if rd > 8:
            add_jh_step.append(did_list[random.randint(0,len(did_list)-1)] + '，' + add_did_step[i])
        else:
            add_jh_step.append(add_did_step[i])


    for i in range(len(add_jh_step)):
        rd = random.randint(1,10)
        if rd > 8:
            if '(0-5)' in add_jh_step[i]:
                add_hw_step.append(jh_0_5_list[random.randint(0,len(jh_0_5_list)-1)] + '，' + add_jh_step[i][5:])
            elif '(5-25)' in add_jh_step[i]:
                add_hw_step.append(jh_5_25_list[random.randint(0,len(jh_5_25_list)-1)] + '，' + add_jh_step[i][6:])
            elif '(25-55)' in add_jh_step[i]:
                add_hw_step.append(jh_25_55_list[random.randint(0,len(jh_25_55_list)-1)] + '，' + add_jh_step[i][7:])
            elif '(55-80)' in add_jh_step[i]:
                add_hw_step.append(jh_55_80_list[random.randint(0,len(jh_55_80_list)-1)] + '，' + add_jh_step[i][7:])
            else:
                add_hw_step.append(jh_list[random.randint(0,len(jh_list)-1)] + '，' + add_jh_step[i])
        else:
            add_hw_step.append(add_jh_step[i])


    for i in range(len(add_hw_step)):
        rd = random.randint(1,10)
        if rd > 9:
            if '(0-5)' in add_hw_step[i]:
                add_sra_step.append(hw_0_5_list[random.randint(0,len(hw_0_5_list)-1)] + '，' + add_hw_step[i][5:])
            elif '(5-25)' in add_hw_step[i]:
                add_sra_step.append(hw_5_25_list[random.randint(0,len(hw_5_25_list)-1)] + '，' + add_hw_step[i][6:])
            elif '(25-55)' in add_hw_step[i]:
                add_sra_step.append(hw_25_55_list[random.randint(0,len(hw_25_55_list)-1)] + '，' + add_hw_step[i][7:])
            elif '(55-80)' in add_hw_step[i]:
                add_sra_step.append(hw_55_80_list[random.randint(0,len(hw_55_80_list)-1)] + '，' + add_hw_step[i][7:])
            else:
                add_sra_step.append(hw_list[random.randint(0,len(hw_list)-1)] + '，' + add_hw_step[i])
        else:
            add_sra_step.append(add_hw_step[i])



    for i in range(len(add_sra_step)):
        rd = random.randint(1,10)
        if rd > 5:
            if '(0-5)' in add_sra_step[i]:
                clean_step.append(sra_0_5_list[random.randint(0,len(sra_0_5_list)-1)][5:] + '，' + add_sra_step[i][5:])
            elif '(5-25)' in add_sra_step[i]:
                clean_step.append(sra_5_25_list[random.randint(0,len(sra_5_25_list)-1)][6:] + '，' + add_sra_step[i][6:])
            elif '(25-55)' in add_sra_step[i]:
                clean_step.append(sra_25_55_list[random.randint(0,len(sra_25_55_list)-1)][7:] + '，' + add_sra_step[i][7:])
            elif '(55-80)' in add_sra_step[i]:
                clean_step.append(sra_55_80_list[random.randint(0,len(sra_55_80_list)-1)][7:] + '，' + add_sra_step[i][7:])
            else:
                rd = random.randint(0,len(sra_list)-1)
                s = sra_list[rd][sra_list[rd].index(')')+1:]
                clean_step.append(s + '，' + add_sra_step[i])
        else:
            clean_step.append(add_sra_step[i])

    for i in range(len(clean_step)):
        if ')' in clean_step[i]:
            clean_step[i] = clean_step[i][clean_step[i].index(')')+1:]
    return clean_step

def create_labelJinjizheng_list():
    sra_list = []
    hw_list = []
    jh_list = []
    custom_list = []
    label_Jinjizheng = []

    jh_0_5_list = []
    jh_5_25_list = []
    jh_25_55_list = []
    jh_55_80_list = []

    hw_0_5_list = []
    hw_5_25_list = []
    hw_25_55_list = []
    hw_55_80_list = []

    sra_0_5_list = []
    sra_5_25_list = []
    sra_25_55_list = []
    sra_55_80_list = []

    add_jh_step = []
    add_hw_step = []
    add_sra_step = []
    clean_step = []


    with open('parts/parts_Jinjizheng/sex_relation+age.txt', encoding='utf-8') as infile:
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

    with open('parts/parts_Jinjizheng/height+weight.txt', encoding='utf-8') as infile:
        i = 0
        for line in infile:
            if i == 0:
                hw_list.append(line[1:-1])
                if '(0-5)' in line:
                    hw_0_5_list.append(line[1:-1])
                elif '(5-25)' in line:
                    hw_5_25_list.append(line[1:-1])
                elif '(25-55)' in line:
                    hw_25_55_list.append(line[1:-1])
                elif '(55-80)' in line:
                    hw_55_80_list.append(line[1:-1])
                i += 1
            else:
                hw_list.append(line[:-1])
                if '(0-5)' in line:
                    hw_0_5_list.append(line[:-1])
                elif '(5-25)' in line:
                    hw_5_25_list.append(line[:-1])
                elif '(25-55)' in line:
                    hw_25_55_list.append(line[:-1])
                elif '(55-80)' in line:
                    hw_55_80_list.append(line[:-1])
    infile.close()


    with open('parts/parts_Jinjizheng/job+history.txt', encoding='utf-8') as infile:
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

    with open('parts/parts_Jinjizheng/custom.txt', encoding='utf-8') as infile:
        i = 0
        for line in infile:
            if i == 0:
                custom_list.append(line[1:-1])
                i += 1
            else:
                custom_list.append(line[:-1])
    infile.close()


    with open('parts/parts_Jinjizheng/label_Jinjizheng_q.txt', encoding='utf-8') as infile:
        
        for line in infile:
            label_Jinjizheng.append(line[:-1])
    infile.close()

    for i in range(200):
        rd = random.randint(1,10)
        if rd > 8:
            add_jh_step.append(custom_list[random.randint(0,len(custom_list)-1)] + '，' + label_Jinjizheng[random.randint(0,len(label_Jinjizheng)-1)])
        else:            
            add_jh_step.append(label_Jinjizheng[random.randint(0,len(label_Jinjizheng)-1)])

    for i in range(len(add_jh_step)):
        rd = random.randint(1,10)
        if rd > 8:
            if '(0-5)' in add_jh_step[i]:
                add_hw_step.append(jh_0_5_list[random.randint(0,len(jh_0_5_list)-1)] + '，' + add_jh_step[i][5:])
            elif '(5-25)' in add_jh_step[i]:
                add_hw_step.append(jh_5_25_list[random.randint(0,len(jh_5_25_list)-1)] + '，' + add_jh_step[i][6:])
            elif '(25-55)' in add_jh_step[i]:
                add_hw_step.append(jh_25_55_list[random.randint(0,len(jh_25_55_list)-1)] + '，' + add_jh_step[i][7:])
            elif '(55-80)' in add_jh_step[i]:
                add_hw_step.append(jh_55_80_list[random.randint(0,len(jh_55_80_list)-1)] + '，' + add_jh_step[i][7:])
            else:
                add_hw_step.append(jh_list[random.randint(0,len(jh_list)-1)] + '，' + add_jh_step[i])
        else:
            add_hw_step.append(add_jh_step[i])


    for i in range(len(add_hw_step)):
        rd = random.randint(1,10)
        if rd > 9:
            if '(0-5)' in add_hw_step[i]:
                add_sra_step.append(hw_0_5_list[random.randint(0,len(hw_0_5_list)-1)] + '，' + add_hw_step[i][5:])
            elif '(5-25)' in add_hw_step[i]:
                add_sra_step.append(hw_5_25_list[random.randint(0,len(hw_5_25_list)-1)] + '，' + add_hw_step[i][6:])
            elif '(25-55)' in add_hw_step[i]:
                add_sra_step.append(hw_25_55_list[random.randint(0,len(hw_25_55_list)-1)] + '，' + add_hw_step[i][7:])
            elif '(55-80)' in add_hw_step[i]:
                add_sra_step.append(hw_55_80_list[random.randint(0,len(hw_55_80_list)-1)] + '，' + add_hw_step[i][7:])
            else:
                add_sra_step.append(hw_list[random.randint(0,len(hw_list)-1)] + '，' + add_hw_step[i])
        else:
            add_sra_step.append(add_hw_step[i])



    for i in range(len(add_sra_step)):
        rd = random.randint(1,10)
        if rd > 5:
            if '(0-5)' in add_sra_step[i]:
                clean_step.append(sra_0_5_list[random.randint(0,len(sra_0_5_list)-1)][5:] + '，' + add_sra_step[i][5:])
            elif '(5-25)' in add_sra_step[i]:
                clean_step.append(sra_5_25_list[random.randint(0,len(sra_5_25_list)-1)][6:] + '，' + add_sra_step[i][6:])
            elif '(25-55)' in add_sra_step[i]:
                clean_step.append(sra_25_55_list[random.randint(0,len(sra_25_55_list)-1)][7:] + '，' + add_sra_step[i][7:])
            elif '(55-80)' in add_sra_step[i]:
                clean_step.append(sra_55_80_list[random.randint(0,len(sra_55_80_list)-1)][7:] + '，' + add_sra_step[i][7:])
            else:
                rd = random.randint(0,len(sra_list)-1)
                s = sra_list[rd][sra_list[rd].index(')')+1:]
                clean_step.append(s + '，' + add_sra_step[i])
        else:
            clean_step.append(add_sra_step[i])

    for i in range(len(clean_step)):
        if ')' in clean_step[i]:
            clean_step[i] = clean_step[i][clean_step[i].index(')')+1:]
    return clean_step

def create_labelTufabingyin_list():
    sra_list = []
    hw_list = []
    jh_list = []
    label_Tufabingyin = []

    hw_0_5_list = []
    hw_5_25_list = []
    hw_25_55_list = []
    hw_55_80_list = []

    sra_0_5_list = []
    sra_5_25_list = []
    sra_25_55_list = []
    sra_55_80_list = []

    add_hw_step = []
    add_sra_step = []
    clean_step = []


    with open('parts/parts_Tufabingyin/sex_relation+age.txt', encoding='utf-8') as infile:
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

    with open('parts/parts_Tufabingyin/height+weight.txt', encoding='utf-8') as infile:
        i = 0
        for line in infile:
            if i == 0:
                hw_list.append(line[1:-1])
                if '(0-5)' in line:
                    hw_0_5_list.append(line[1:-1])
                elif '(5-25)' in line:
                    hw_5_25_list.append(line[1:-1])
                elif '(25-55)' in line:
                    hw_25_55_list.append(line[1:-1])
                elif '(55-80)' in line:
                    hw_55_80_list.append(line[1:-1])
                i += 1
            else:
                hw_list.append(line[:-1])
                if '(0-5)' in line:
                    hw_0_5_list.append(line[:-1])
                elif '(5-25)' in line:
                    hw_5_25_list.append(line[:-1])
                elif '(25-55)' in line:
                    hw_25_55_list.append(line[:-1])
                elif '(55-80)' in line:
                    hw_55_80_list.append(line[:-1])
    infile.close()


    with open('parts/parts_Tufabingyin/job+history.txt', encoding='utf-8') as infile:
        i = 0
        for line in infile:
            if i == 0:
                jh_list.append(line[1:-1])
                i += 1
            else:
                jh_list.append(line[:-1])
    infile.close()

    with open('parts/parts_Tufabingyin/label_Tufabingyin_q.txt', encoding='utf-8') as infile:
        for line in infile:
            label_Tufabingyin.append(line[:-1])
    infile.close()

    for i in range(200):
        rd = random.randint(1,10)
        if rd > 7:
            add_hw_step.append(jh_list[random.randint(0,len(jh_list)-1)] + '，' + label_Tufabingyin[random.randint(0,len(label_Tufabingyin)-1)])
        else:            
            add_hw_step.append(label_Tufabingyin[random.randint(0,len(label_Tufabingyin)-1)])


    for i in range(len(add_hw_step)):
        rd = random.randint(1,10)
        if rd > 9:
            if '(0-5)' in add_hw_step[i]:
                add_sra_step.append(hw_0_5_list[random.randint(0,len(hw_0_5_list)-1)] + '，' + add_hw_step[i][5:])
            elif '(5-25)' in add_hw_step[i]:
                add_sra_step.append(hw_5_25_list[random.randint(0,len(hw_5_25_list)-1)] + '，' + add_hw_step[i][6:])
            elif '(25-55)' in add_hw_step[i]:
                add_sra_step.append(hw_25_55_list[random.randint(0,len(hw_25_55_list)-1)] + '，' + add_hw_step[i][7:])
            elif '(55-80)' in add_hw_step[i]:
                add_sra_step.append(hw_55_80_list[random.randint(0,len(hw_55_80_list)-1)] + '，' + add_hw_step[i][7:])
            else:
                add_sra_step.append(hw_list[random.randint(0,len(hw_list)-1)] + '，' + add_hw_step[i])
        else:
            add_sra_step.append(add_hw_step[i])



    for i in range(len(add_sra_step)):
        rd = random.randint(1,10)
        if rd > 5:
            if '(0-5)' in add_sra_step[i]:
                clean_step.append(sra_0_5_list[random.randint(0,len(sra_0_5_list)-1)][5:] + '，' + add_sra_step[i][5:])
            elif '(5-25)' in add_sra_step[i]:
                clean_step.append(sra_5_25_list[random.randint(0,len(sra_5_25_list)-1)][6:] + '，' + add_sra_step[i][6:])
            elif '(25-55)' in add_sra_step[i]:
                clean_step.append(sra_25_55_list[random.randint(0,len(sra_25_55_list)-1)][7:] + '，' + add_sra_step[i][7:])
            elif '(55-80)' in add_sra_step[i]:
                clean_step.append(sra_55_80_list[random.randint(0,len(sra_55_80_list)-1)][7:] + '，' + add_sra_step[i][7:])
            else:
                rd = random.randint(0,len(sra_list)-1)
                s = sra_list[rd][sra_list[rd].index(')')+1:]
                clean_step.append(s + '，' + add_sra_step[i])
        else:
            clean_step.append(add_sra_step[i])

    for i in range(len(clean_step)):
        if ')' in clean_step[i]:
            clean_step[i] = clean_step[i][clean_step[i].index(')')+1:]
    return clean_step

def do_create_2hop(list1,list2,i1,i2):
    label_Zhengduanguanxi = '诊断关系;'
    label_Bingfa = '并发、合并;'
    label_Tuijiankeshi = '推荐科室;'
    label_Peiwuguanxi = '配伍关系;'
    label_Fashengbuwei = '发生部位;'
    label_Jinjizheng = '禁忌证;'
    label_Buliangfanying = '不良反应;'
    label_Huanbingqingxiang = '患病倾向、发病原因;'
    label_Jibingfenqi = '疾病分期、分级、分型;'
    label_Linchuangbiaoxian = '临床表现;'
    label_Shiyingzheng = '适应证;'

    label_vec = [label_Zhengduanguanxi, label_Bingfa, label_Tuijiankeshi, label_Peiwuguanxi, label_Fashengbuwei, label_Jinjizheng, label_Buliangfanying, label_Huanbingqingxiang, label_Jibingfenqi, label_Linchuangbiaoxian, label_Shiyingzheng]

    dataset_list = []
    sentence_list = []
    label_list = []
    lbl = []
    lbl_list = []
    if i1 == 0 or i2 == 0:
        lbl.append(label_vec[0])
    if i1 == 1 or i2 == 1:
        lbl.append(label_vec[1])
    if i1 == 2 or i2 == 2:
        lbl.append(label_vec[2])
    if i1 == 3 or i2 == 3:
        lbl.append(label_vec[3])
    if i1 == 4 or i2 == 4:
        lbl.append(label_vec[4])
    if i1 == 5 or i2 == 5:
        lbl.append(label_vec[5])
    if i1 == 6 or i2 == 6:
        lbl.append(label_vec[6])
    if i1 == 7 or i2 == 7:
        lbl.append(label_vec[7])
    if i1 == 8 or i2 == 8:
        lbl.append(label_vec[8])
    if i1 == 9 or i2 == 9:
        lbl.append(label_vec[9])
    if i1 == 10 or i2 == 10:
        lbl.append(label_vec[10])
    for i in range(300):
        sent1 = random.randint(0,len(list1)-1)
        sent2 = random.randint(0,len(list2)-1)
        if [sent1, sent2] not in dataset_list:
            sentence = list1[sent1] + list2[sent2]
            sentence_list.append(sentence)
            dataset_list.append([sent1, sent2])
            lbl_list.append(lbl)
        else:
            continue
    return sentence_list, lbl_list

def do_create_3hop(list1,list2,list3,i1,i2,i3):
    label_Zhengduanguanxi = '诊断关系;'
    label_Bingfa = '并发、合并;'
    label_Tuijiankeshi = '推荐科室;'
    label_Peiwuguanxi = '配伍关系;'
    label_Fashengbuwei = '发生部位;'
    label_Jinjizheng = '禁忌证;'
    label_Buliangfanying = '不良反应;'
    label_Huanbingqingxiang = '患病倾向、发病原因;'
    label_Jibingfenqi = '疾病分期、分级、分型;'
    label_Linchuangbiaoxian = '临床表现;'
    label_Shiyingzheng = '适应证;'

    label_vec = [label_Zhengduanguanxi, label_Bingfa, label_Tuijiankeshi, label_Peiwuguanxi, label_Fashengbuwei, label_Jinjizheng, label_Buliangfanying, label_Huanbingqingxiang, label_Jibingfenqi, label_Linchuangbiaoxian, label_Shiyingzheng]


    dataset_list = []
    sentence_list = []
    label_list = []
    lbl = []
    lbl_list = []
    if i1 == 0 or i2 == 0 or i3 == 0:
        lbl.append(label_vec[0])
    if i1 == 1 or i2 == 1 or i3 == 1:
        lbl.append(label_vec[1])
    if i1 == 2 or i2 == 2 or i3 == 2:
        lbl.append(label_vec[2])
    if i1 == 3 or i2 == 3 or i3 == 3:
        lbl.append(label_vec[3])
    if i1 == 4 or i2 == 4 or i3 == 4:
        lbl.append(label_vec[4])
    if i1 == 5 or i2 == 5 or i3 == 5:
        lbl.append(label_vec[5])
    if i1 == 6 or i2 == 6 or i3 == 6:
        lbl.append(label_vec[6])
    if i1 == 7 or i2 == 7 or i3 == 7:
        lbl.append(label_vec[7])
    if i1 == 8 or i2 == 8 or i3 == 8:
        lbl.append(label_vec[8])
    if i1 == 9 or i2 == 9 or i3 == 9:
        lbl.append(label_vec[9])
    if i1 == 10 or i2 == 10 or i3 == 10:
        lbl.append(label_vec[10])
    for i in range(100):
        sent1 = random.randint(0,len(list1)-1)
        sent2 = random.randint(0,len(list2)-1)
        sent3 = random.randint(0,len(list3)-1)
        if [sent1, sent2,sent3] not in dataset_list:
            sentence = list1[sent1] + list2[sent2] + list3[sent3]
            sentence_list.append(sentence)
            dataset_list.append([sent1, sent2,sent3])
            lbl_list.append(lbl)
        else:
            continue
    return sentence_list, lbl_list

def create_file():
    Zhengduanguanxi_list = create_labelZhengduanguanxi_list()
    
    Bingfa_list = []
    with open('parts/parts_Bingfa/label_Bingfa_q.txt', 'r', encoding='utf-8') as infile:
        for line in infile:
            Bingfa_list.append(line[:-1])

    Tuijiankeshi_list = []
    with open('parts/parts_Tuijiankeshi/label_Tuijiankeshi_q.txt', 'r', encoding='utf-8') as infile:
        for line in infile:
            Tuijiankeshi_list.append(line[:-1])


    Peiwuguanxi_list = []
    with open('parts/parts_Peiwuguanxi/label_Peiwuguanxi_q.txt', 'r', encoding='utf-8') as infile:
        for line in infile:
            Peiwuguanxi_list.append(line[:-1])


    Fashengbuwei_list = []
    with open('parts/parts_Fashengbuwei/label_Fashengbuwei_q.txt', 'r', encoding='utf-8') as infile:
        for line in infile:
            Fashengbuwei_list.append(line[:-1])

    Jinjizheng_list = create_labelJinjizheng_list()
    
    Buliangfanying_list = []
    with open('parts/parts_Buliangfanying/label_Buliangfanying_q.txt', 'r', encoding='utf-8') as infile:
        for line in infile:
            Buliangfanying_list.append(line[:-1])


    Huanbingqingxiang_list = create_labelTufabingyin_list()
    with open('parts/parts_Huanbingqingxiang/label_Huanbingqingxiang_q.txt', 'r', encoding='utf-8') as infile:
        for line in infile:
            Huanbingqingxiang_list.append(line[:-1])
    
    Jibingfenqi_list = []
    with open('parts/parts_Jibingfenqi/label_Jibingfenqi_q.txt', 'r', encoding='utf-8') as infile:
        for line in infile:
            Jibingfenqi_list.append(line[:-1])


    Linchuangbiaoxian_list = []
    with open('parts/parts_Linchuangbiaoxian/label_Linchuangbiaoxian_q.txt', 'r', encoding='utf-8') as infile:
        for line in infile:
            Linchuangbiaoxian_list.append(line[:-1])

    Shiyingzheng_list = []
    with open('parts/parts_Shiyingzheng/label_Shiyingzheng_q.txt', 'r', encoding='utf-8') as infile:
        for line in infile:
            Shiyingzheng_list.append(line[:-1])
    

    





    dataset = []
    label = []
    label_Zhengduanguanxi = '诊断关系;'
    label_Bingfa = '并发、合并;'
    label_Tuijiankeshi = '推荐科室;'
    label_Peiwuguanxi = '配伍关系;'
    label_Fashengbuwei = '发生部位;'
    label_Jinjizheng = '禁忌证;'
    label_Buliangfanying = '不良反应;'
    label_Huanbingqingxiang = '患病倾向、发病原因;'
    label_Jibingfenqi = '疾病分期、分级、分型;'
    label_Linchuangbiaoxian = '临床表现;'
    label_Shiyingzheng = '适应证;'

    label_vec = [Zhengduanguanxi_list, Bingfa_list, Tuijiankeshi_list, Peiwuguanxi_list, Fashengbuwei_list, Jinjizheng_list, Buliangfanying_list, Huanbingqingxiang_list, Jibingfenqi_list, Linchuangbiaoxian_list, Shiyingzheng_list]

    label_name_vec = [label_Zhengduanguanxi, label_Bingfa, label_Tuijiankeshi, label_Peiwuguanxi, label_Fashengbuwei, label_Jinjizheng, label_Buliangfanying, label_Huanbingqingxiang, label_Jibingfenqi, label_Linchuangbiaoxian, label_Shiyingzheng]

    # 2-hop
    for i in range(10):
        for j in range(11-i-1):
            s,l = do_create_2hop(label_vec[i], label_vec[11-j-2], i, 11-j-2)
            dataset += s
            label += l
            s,l = do_create_2hop(label_vec[11-j-2], label_vec[i], 11-j-2, i)
            dataset += s
            label += l

    # 1-hop
    for i in range(11):
        for j in range(len(label_vec[i])):
            dataset.append(label_vec[i][j])
            
            label.append(label_name_vec[i])

    # 3-hop
    for i in range(9):
        for j in range(11-i-1):
            for k in range(11-i-j-2):
                s,l = do_create_3hop(label_vec[i], label_vec[11-j-1], label_vec[11-j-k-2], i, 11-j-1, 11-j-k-2)
                dataset += s
                label += l
                s,l = do_create_3hop(label_vec[i], label_vec[11-j-k-2], label_vec[11-j-1], i, 11-j-k-2, 11-j-1)
                dataset += s
                label += l
                s,l = do_create_3hop(label_vec[11-j-1], label_vec[i], label_vec[11-j-k-2], 11-j-1, i, 11-j-k-2)
                dataset += s
                label += l
                s,l = do_create_3hop(label_vec[11-j-1], label_vec[11-j-k-2], label_vec[i], 11-j-1, 11-j-k-2, i)
                dataset += s
                label += l
                s,l = do_create_3hop(label_vec[11-j-k-2], label_vec[i], label_vec[11-j-1], 11-j-k-2, i, 11-j-1)
                dataset += s
                label += l

                s,l = do_create_3hop(label_vec[11-j-k-2], label_vec[11-j-1], label_vec[i], 11-j-k-2, 11-j-1, i)
                dataset += s
                label += l

    
    li=list(range(len(dataset)))  
    random.shuffle(li)  
    
    dataset = [x for _,x in sorted(zip(li,dataset))]
    label = [x for _,x in sorted(zip(li,label))]

    with open('test.txt', 'w', encoding='utf-8') as outfile:
        for line in dataset[0:10000]:
            outfile.write(line+'\n')
        
    outfile.close()
    
    with open('test_label.txt', 'w', encoding='utf-8') as outfile:
        for line in label[0:10000]:
            outfile.write(''.join(e for e in line) + '\n')
    outfile.close()

    with open('val.txt', 'w', encoding='utf-8') as outfile:
        for line in dataset[10001:20000]:
            outfile.write(line+'\n')
        
    outfile.close()

    with open('val_label.txt', 'w', encoding='utf-8') as outfile:
        for line in label[10001:20000]:
            outfile.write(''.join(e for e in line) + '\n')
    outfile.close()

    with open('train.txt', 'w', encoding='utf-8') as outfile:
        for line in dataset[20001:]:
            outfile.write(line+'\n')
        
    outfile.close()

    with open('train_label.txt', 'w', encoding='utf-8') as outfile:
        for line in label[20001:]:
            outfile.write(''.join(e for e in line) + '\n')
    outfile.close()
    

def main():
    create_file()


if __name__ == '__main__':
    main()