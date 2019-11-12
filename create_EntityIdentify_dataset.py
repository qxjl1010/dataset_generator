# -*- coding: UTF-8 -*-
import random
import re


def create_tag1_list():
    sra_list = []
    jh_list = []
    did_list = []
    tl_list = []
    label_1_l = []

    sra_list_tag = []
    jh_list_tag = []
    did_list_tag = []
    tl_list_tag = []
    label_1_l_tag = []

    jh_0_5_list = []
    jh_5_25_list = []
    jh_25_55_list = []
    jh_55_80_list = []

    jh_0_5_list_tag = []
    jh_5_25_list_tag = []
    jh_25_55_list_tag = []
    jh_55_80_list_tag = []

    sra_0_5_list = []
    sra_5_25_list = []
    sra_25_55_list = []
    sra_55_80_list = []

    sra_0_5_list_tag = []
    sra_5_25_list_tag = []
    sra_25_55_list_tag = []
    sra_55_80_list_tag = []

    step_1_list = []
    step_2_list = []
    step_3_list = []
    step_4_list = []
    step_5_list = []

    step_1_list_tag = []
    step_2_list_tag = []
    step_3_list_tag = []
    step_4_list_tag = []
    step_5_list_tag = []

    disease_list = []
    symptom_list = []
    drug_list = []

    with open('disease.txt', encoding='utf-8') as infile:
        for line in infile:
            disease_list.append(line[:-2])


    with open('symptoms.txt', encoding='utf-8') as infile:
        for line in infile:
            symptom_list.append(line[:-2])


    with open('drug.txt', encoding='utf-8') as infile:
        for line in infile:
            if len(line[:-2]) <= 1:
                continue
            drug_list.append(line[:-2])
   

    with open('parts/parts_Zhengduanguanxi/sex_relation+age.txt', encoding='utf-8') as infile1, open('parts/parts_Zhengduanguanxi/sex_relation+age_tag.txt', encoding='utf-8') as infile2:
        i = 0
        for line1,line2 in zip(infile1, infile2):
            
            line2 = line2[:-1].split(',')
            if i == 0:
                disease_rd = random.randint(0,len(disease_list)-1)
                symptom_rd = random.randint(0,len(symptom_list)-1)
                line_1 = line1[line1.index(')')+1:]
                have_dis = [have_dis.start() for have_dis in re.finditer('DIS', line_1)]
                
                if len(have_dis) != 0:
                    for j in range(len(have_dis)):
                        dis = []
                        for k in range(len(disease_list[disease_rd])-2):
                            dis += ['I-D']
                        dis = ['B-D'] + dis + ['E-D']
                        line2[have_dis[j]:have_dis[j]+1] = iter(dis)
                        # line2[have_dis[j]] = dis
                have_spt = [have_spt.start() for have_spt in re.finditer('SPT', line_1)]
                if len(have_spt) != 0:
                    for j in range(len(have_spt)):
                        spt = []
                        for k in range(len(symptom_list[symptom_rd])-2):
                            spt += ['I-S']
                        spt = ['B-S'] + spt + [',E-S']
                        line2[have_spt[j]:have_spt[j]+1] = iter(spt)
                        # line2[have_spt[j]] = spt
                
                inserted_q = line1[1:-1].replace('DIS',disease_list[disease_rd])
                inserted_q = inserted_q.replace('SPT',symptom_list[symptom_rd])
                sra_list.append(inserted_q)
                
                line_2 = ''
                for j in range(len(line2)):
                    line_2 = line_2 + line2[j] + ',' 

                # sra_list_tag.append(line_2[:-1])
                sra_list_tag.append(line2)
                if '(0-5)' in line1:
                    sra_0_5_list.append(inserted_q)
                    #sra_0_5_list_tag.append(line_2)
                    sra_0_5_list_tag.append(line2)
                elif '(5-25)' in line1:
                    sra_5_25_list.append(inserted_q)
                    #sra_5_25_list_tag.append(line_2)
                    sra_5_25_list_tag.append(line2)
                elif '(25-55)' in line1:
                    sra_25_55_list.append(inserted_q)
                    #sra_25_55_list_tag.append(line_2)
                    sra_25_55_list_tag.append(line2)
                elif '(55-80)' in line1:
                    sra_55_80_list.append(inserted_q)
                    #sra_55_80_list_tag.append(line_2)
                    sra_55_80_list_tag.append(line2)
                i += 1
            else:
                disease_rd = random.randint(0,len(disease_list)-1)
                symptom_rd = random.randint(0,len(symptom_list)-1)
                line_1 = line1[line1.index(')')+1:]
                have_dis = [have_dis.start() for have_dis in re.finditer('DIS', line_1)]
                if len(have_dis) != 0:
                    for j in range(len(have_dis)):
                        dis = []
                        for k in range(len(disease_list[disease_rd])-2):
                            dis += ['I-D']
                        dis = ['B-D'] + dis + ['E-D']
                        line2[have_dis[j]:have_dis[j]+1] = iter(dis)
                have_spt = [have_spt.start() for have_spt in re.finditer('SPT', line_1)]
                if len(have_spt) != 0:
                    for j in range(len(have_spt)):
                        spt = []
                        for k in range(len(symptom_list[symptom_rd])-2):
                            spt += ['I-S']
                        spt = ['B-S'] + spt + ['E-S']
                        line2[have_spt[j]:have_spt[j]+1] = iter(spt)

                line_2 = ''
                for j in range(len(line2)):
                    line_2 = line_2 + line2[j] + ',' 
                
                inserted_q = line1[:-1].replace('DIS',disease_list[disease_rd])
                inserted_q = inserted_q.replace('SPT',symptom_list[symptom_rd])
                sra_list.append(inserted_q)
                sra_list_tag.append(line2)
                #sra_list_tag.append(line_2[:-1])
                if '(0-5)' in line1:
                    sra_0_5_list.append(inserted_q)
                    #sra_0_5_list_tag.append(line_2[:-1])
                    sra_0_5_list_tag.append(line2)
                elif '(5-25)' in line1:
                    sra_5_25_list.append(inserted_q)
                    #sra_5_25_list_tag.append(line_2[:-1])
                    sra_5_25_list_tag.append(line2)
                elif '(25-55)' in line1:
                    sra_25_55_list.append(inserted_q)
                    #sra_25_55_list_tag.append(line_2[:-1])
                    sra_25_55_list_tag.append(line2)
                elif '(55-80)' in line1:
                    sra_55_80_list.append(inserted_q)
                    #sra_55_80_list_tag.append(line_2[:-1])
                    sra_55_80_list_tag.append(line2)


    
    with open('parts/parts_Zhengduanguanxi/job+history.txt', encoding='utf-8') as infile1, open('parts/parts_Zhengduanguanxi/job+history_tag.txt', encoding='utf-8') as infile2:
        i = 0
        for line1,line2 in zip(infile1, infile2):
            
            line2 = line2[:-1].split(',')
            if i == 0:
                disease_rd = random.randint(0,len(disease_list)-1)
                symptom_rd = random.randint(0,len(symptom_list)-1)
                drug_rd = random.randint(0,len(drug_list)-1)
                line_1 = line1[line1.index(')')+1:]
                have_dis = [have_dis.start() for have_dis in re.finditer('DIS', line_1)]
                
                if len(have_dis) != 0:
                    for j in range(len(have_dis)):
                        dis = []
                        for k in range(len(disease_list[disease_rd])-2):
                            dis += ['I-D']
                        dis = ['B-D'] + dis + ['E-D']
                        line2[have_dis[j]:have_spt[j]+1] = iter(dis)
                        # line2[have_dis[j]] = dis
                have_spt = [have_spt.start() for have_spt in re.finditer('SPT', line_1)]
                if len(have_spt) != 0:
                    for j in range(len(have_spt)):
                        spt = []
                        for k in range(len(symptom_list[symptom_rd])-2):
                            spt += ['I-S']
                        spt = ['B-S'] + spt + ['E-S']
                        line2[have_spt[j]:have_spt[j]+1] = iter(spt)
                        # line2[have_spt[j]] = spt
                
                have_drug = [have_drug.start() for have_drug in re.finditer('MED', line_1)]
                if len(have_drug) != 0:
                    for j in range(len(have_drug)):
                        med = []
                        for k in range(len(drug_list[drug_rd])-2):
                            med += ['I-M']
                        med = ['B-M'] + med + ['E-M']
                        line2[have_drug[j]:have_drug[j]+1] = iter(med)


                inserted_q = line1[1:-1].replace('DIS',disease_list[disease_rd])
                inserted_q = inserted_q.replace('SPT',symptom_list[symptom_rd])
                inserted_q = inserted_q.replace('MED',drug_list[drug_rd])
                jh_list.append(inserted_q)
                
                line_2 = ''
                for j in range(len(line2)):
                    line_2 = line_2 + line2[j] + ',' 

                # jh_list_tag.append(line_2[:-1])
                jh_list_tag.append(line2)
                if '(0-5)' in line1:
                    jh_0_5_list.append(inserted_q)
                    #jh_0_5_list_tag.append(line_2)
                    jh_0_5_list_tag.append(line2)
                elif '(5-25)' in line1:
                    jh_5_25_list.append(inserted_q)
                    #jh_5_25_list_tag.append(line_2)
                    jh_5_25_list_tag.append(line2)
                elif '(25-55)' in line1:
                    jh_25_55_list.append(inserted_q)
                    #jh_25_55_list_tag.append(line_2)
                    jh_25_55_list_tag.append(line2)
                elif '(55-80)' in line1:
                    jh_55_80_list.append(inserted_q)
                    #jh_55_80_list_tag.append(line_2)
                    jh_55_80_list_tag.append(line2)
                i += 1
            else:
                disease_rd = random.randint(0,len(disease_list)-1)
                symptom_rd = random.randint(0,len(symptom_list)-1)
                drug_rd = random.randint(0,len(drug_list)-1)
                line_1 = line1[line1.index(')')+1:]
                have_dis = [have_dis.start() for have_dis in re.finditer('DIS', line_1)]
                if len(have_dis) != 0:
                    for j in range(len(have_dis)):
                        dis = []
                        for k in range(len(disease_list[disease_rd])-2):
                            dis += ['I-D']
                        dis = ['B-D'] + dis + ['E-D']

                        line2[have_dis[j]:have_dis[j]+1] = iter(dis)
                        # line2[have_dis[j]] = dis
                have_spt = [have_spt.start() for have_spt in re.finditer('SPT', line_1)]
                if len(have_spt) != 0:
                    for j in range(len(have_spt)):
                        spt = []
                        for k in range(len(symptom_list[symptom_rd])-2):
                            spt += ['I-S']
                        spt = ['B-S'] + spt + ['E-S']
                        line2[have_spt[j]:have_spt[j]+1] = iter(spt)
                        # line2[have_spt[j]] = spt
                have_drug = [have_drug.start() for have_drug in re.finditer('MED', line_1)]
                if len(have_drug) != 0:
                    for j in range(len(have_drug)):
                        med = []
                        for k in range(len(drug_list[drug_rd])-2):
                            med += ['I-M']
                        med = ['B-M'] + med + ['E-M']
                        line2[have_drug[j]:have_drug[j]+1] = iter(med)
                inserted_q = line1[:-1].replace('DIS',disease_list[disease_rd])
                inserted_q = inserted_q.replace('SPT',symptom_list[symptom_rd])
                inserted_q = inserted_q.replace('MED',drug_list[drug_rd])
                jh_list.append(inserted_q)
                #jh_list_tag.append(line_2[:-1])
                jh_list_tag.append(line2)
                if '(0-5)' in line1:
                    jh_0_5_list.append(inserted_q)
                    # jh_0_5_list_tag.append(line_2[:-1])
                    jh_0_5_list_tag.append(line2)
                elif '(5-25)' in line1:
                    jh_5_25_list.append(inserted_q)
                    #jh_5_25_list_tag.append(line_2[:-1])
                    jh_5_25_list_tag.append(line2)
                elif '(25-55)' in line1:
                    jh_25_55_list.append(inserted_q)
                    #jh_25_55_list_tag.append(line_2[:-1])
                    jh_25_55_list_tag.append(line2)
                elif '(55-80)' in line1:
                    jh_55_80_list.append(inserted_q)
                    #jh_55_80_list_tag.append(line_2[:-1])
                    jh_55_80_list_tag.append(line2)

    with open('parts/parts_Zhengduanguanxi/did.txt', encoding='utf-8') as infile1, open('parts/parts_Zhengduanguanxi/did_tag.txt', encoding='utf-8') as infile2:
        i = 0
        for line1,line2 in zip(infile1, infile2):
            
            line2 = line2[:-1].split(',')
            if i == 0:
                disease_rd = random.randint(0,len(disease_list)-1)
                symptom_rd = random.randint(0,len(symptom_list)-1)
                line_1 = line1[line1.index(')')+1:]
                have_dis = [have_dis.start() for have_dis in re.finditer('DIS', line_1)]
                
                if len(have_dis) != 0:
                    for j in range(len(have_dis)):
                        dis = []
                        for k in range(len(disease_list[disease_rd])-2):
                            dis += ['I-D']
                        dis = ['B-D'] + dis + ['E-D']
                        line2[have_dis[j]:have_dis[j]+1] = iter(dis)
                have_spt = [have_spt.start() for have_spt in re.finditer('SPT', line_1)]
                if len(have_spt) != 0:
                    for j in range(len(have_spt)):
                        spt = []
                        for k in range(len(symptom_list[symptom_rd])-2):
                            spt += ['I-S']
                        spt = ['B-S'] + spt + ['E-S']
                        line2[have_spt[j]:have_spt[j]+1] = iter(spt)
                
                inserted_q = line1[1:-1].replace('DIS',disease_list[disease_rd])
                inserted_q = inserted_q.replace('SPT',symptom_list[symptom_rd])
                did_list.append(inserted_q)
                
                line_2 = ''
                for j in range(len(line2)):
                    line_2 = line_2 + line2[j] + ',' 

                #did_list_tag.append(line_2[:-1])
                did_list_tag.append(line2)
                i += 1
            else:
                disease_rd = random.randint(0,len(disease_list)-1)
                symptom_rd = random.randint(0,len(symptom_list)-1)
                line_1 = line1[line1.index(')')+1:]
                have_dis = [have_dis.start() for have_dis in re.finditer('DIS', line_1)]
                if len(have_dis) != 0:
                    for j in range(len(have_dis)):
                        dis = []
                        for k in range(len(disease_list[disease_rd])-2):
                            dis += ['I-D']
                        dis = ['B-D'] + dis + ['E-D']
                        line2[have_dis[j]:have_dis[j]+1] = iter(dis)
                have_spt = [have_spt.start() for have_spt in re.finditer('SPT', line_1)]
                if len(have_spt) != 0:
                    for j in range(len(have_spt)):
                        spt = []
                        for k in range(len(symptom_list[symptom_rd])-2):
                            spt += ['I-S']
                        spt = ['B-S'] + spt + ['E-S']
                        line2[have_spt[j]:have_spt[j]+1] = iter(spt)

                line_2 = ''
                for j in range(len(line2)):
                    line_2 = line_2 + line2[j] + ',' 
                
                inserted_q = line1[:-1].replace('DIS',disease_list[disease_rd])
                inserted_q = inserted_q.replace('SPT',symptom_list[symptom_rd])
                did_list.append(inserted_q)
                #did_list_tag.append(line_2[:-1])
                did_list_tag.append(line2)

    with open('parts/parts_Zhengduanguanxi/time+location.txt', encoding='utf-8') as infile1, open('parts/parts_Zhengduanguanxi/time+location_tag.txt', encoding='utf-8') as infile2:
        i = 0
        for line1,line2 in zip(infile1, infile2):
            
            line2 = line2[:-1].split(',')
            if i == 0:
                disease_rd = random.randint(0,len(disease_list)-1)
                symptom_rd = random.randint(0,len(symptom_list)-1)
                have_dis = [have_dis.start() for have_dis in re.finditer('DIS', line1)]
                
                if len(have_dis) != 0:
                    for j in range(len(have_dis)):
                        dis = []
                        for k in range(len(disease_list[disease_rd])-2):
                            dis += ['I-D']
                        dis = ['B-D'] + dis + ['E-D']
                        line2[have_dis[j]:have_dis[j]+1] = iter(dis)
                have_spt = [have_spt.start() for have_spt in re.finditer('SPT', line1)]
                if len(have_spt) != 0:
                    for j in range(len(have_spt)):
                        spt = []
                        for k in range(len(symptom_list[symptom_rd])-2):
                            spt += ['I-S']
                        spt = ['B-S'] + spt + ['E-S']
                        line2[have_spt[j]:have_spt[j]+1] = iter(spt)
                
                inserted_q = line1[1:-1].replace('DIS',disease_list[disease_rd])
                inserted_q = inserted_q.replace('SPT',symptom_list[symptom_rd])
                tl_list.append(inserted_q)
                
                line_2 = ''
                for j in range(len(line2)):
                    line_2 = line_2 + line2[j] + ',' 

                #tl_list_tag.append(line_2[:-1])
                tl_list_tag.append(line2)
                i += 1
            else:
                disease_rd = random.randint(0,len(disease_list)-1)
                symptom_rd = random.randint(0,len(symptom_list)-1)
                have_dis = [have_dis.start() for have_dis in re.finditer('DIS', line1)]
                if len(have_dis) != 0:
                    for j in range(len(have_dis)):
                        dis = []
                        for k in range(len(disease_list[disease_rd])-2):
                            dis += ['I-D']
                        dis = ['B-D'] + dis + ['E-D']
                        line2[have_dis[j]:have_dis[j]+1] = iter(dis)
                have_spt = [have_spt.start() for have_spt in re.finditer('SPT', line1)]
                if len(have_spt) != 0:
                    for j in range(len(have_spt)):
                        spt = []
                        for k in range(len(symptom_list[symptom_rd])-2):
                            spt += ['I-S']
                        spt = ['B-S'] + spt + ['E-S']
                        line2[have_spt[j]:have_spt[j]+1] = iter(spt)

                line_2 = ''
                for j in range(len(line2)):
                    line_2 = line_2 + line2[j] + ',' 
                
                inserted_q = line1[:-1].replace('DIS',disease_list[disease_rd])
                inserted_q = inserted_q.replace('SPT',symptom_list[symptom_rd])
                tl_list.append(inserted_q)
                #tl_list_tag.append(line_2[:-1])
                tl_list_tag.append(line2)

    
    with open('parts/parts_Zhengduanguanxi/label_1_q.txt', encoding='utf-8') as infile1, open('parts/parts_Zhengduanguanxi/label_1_q_tag.txt', encoding='utf-8') as infile2:
        i = 0
        for line1,line2 in zip(infile1, infile2):
            
            line2 = line2[:-1].split(',')
            if i == 0:
                disease_rd = random.randint(0,len(disease_list)-1)
                symptom_rd = random.randint(0,len(symptom_list)-1)
                have_dis = [have_dis.start() for have_dis in re.finditer('DIS', line1)]
                
                if len(have_dis) != 0:
                    for j in range(len(have_dis)):
                        dis = []
                        for k in range(len(disease_list[disease_rd])-2):
                            dis += ['I-D']
                        dis = ['B-D'] + dis + ['E-D']
                        line2[have_dis[j]:have_dis[j]+1] = iter(dis)
                have_spt = [have_spt.start() for have_spt in re.finditer('SPT', line1)]
                if len(have_spt) != 0:
                    for j in range(len(have_spt)):
                        spt = []
                        for k in range(len(symptom_list[symptom_rd])-2):
                            spt += ['I-S']
                        spt = ['B-S'] + spt + ['E-S']
                        line2[have_spt[j]:have_spt[j]+1] = iter(spt)
                
                inserted_q = line1[1:-1].replace('DIS',disease_list[disease_rd])
                inserted_q = inserted_q.replace('SPT',symptom_list[symptom_rd])
                label_1_l.append(inserted_q)
                
                line_2 = ''
                for j in range(len(line2)):
                    line_2 = line_2 + line2[j] + ',' 

                #label_1_l_tag.append(line_2[:-1])
                label_1_l_tag.append(line2)
                i += 1
            else:
                disease_rd = random.randint(0,len(disease_list)-1)
                symptom_rd = random.randint(0,len(symptom_list)-1)
                have_dis = [have_dis.start() for have_dis in re.finditer('DIS', line1)]
                if len(have_dis) != 0:
                    for j in range(len(have_dis)):
                        dis = []
                        for k in range(len(disease_list[disease_rd])-2):
                            dis += ['I-D']
                        dis = ['B-D'] + dis + ['E-D']
                        line2[have_dis[j]:have_dis[j]+1] = iter(dis)
                have_spt = [have_spt.start() for have_spt in re.finditer('SPT', line1)]
                if len(have_spt) != 0:
                    for j in range(len(have_spt)):
                        spt = []
                        for k in range(len(symptom_list[symptom_rd])-2):
                            spt += ['I-S']
                        spt = ['B-S'] + spt + ['E-S']
                        line2[have_spt[j]:have_spt[j]+1] = iter(spt)

                
                inserted_q = line1[:-1].replace('DIS',disease_list[disease_rd])
                inserted_q = inserted_q.replace('SPT',symptom_list[symptom_rd])
                label_1_l.append(inserted_q)
                #label_1_l_tag.append(line_2[:-1])
                label_1_l_tag.append(line2)
    
    
    for i in range(100):
        STP_num = random.randint(1,3)
        STP_part = ''        
        
        spt = []

        for i in range(STP_num):
            symptom_rd = random.randint(0,len(symptom_list)-1)
            STP_part = STP_part + symptom_list[symptom_rd] + '，'
            spt_tmp = []
            spt_tmp2 = []
            # get target of STP
        
            for k in range(len(symptom_list[symptom_rd])-2):
                spt_tmp += ['I-S']
            spt_tmp2 += ['B-S']
            spt_tmp2 += spt_tmp
            spt_tmp2 += ['E-S']
            spt_tmp2 += ['O']
            spt += spt_tmp2   
        picked_label_1 = random.randint(0,len(label_1_l)-1)
        step_1_list.append(STP_part + label_1_l[picked_label_1])

        
        step_1_list_tag.append(spt + label_1_l_tag[picked_label_1])

    
    for i in range(len(step_1_list)):
        rd = random.randint(1,10)
        if rd > 8:
            rd_picked = random.randint(0,len(tl_list)-1)
            step_2_list.append(tl_list[rd_picked] + '，' + step_1_list[i])
            tmp = []

            tmp += tl_list_tag[rd_picked]
            tmp += ['O']
            tmp += step_1_list_tag[i]
            step_2_list_tag.append(tmp)
        else:
            step_2_list.append(step_1_list[i])
            step_2_list_tag.append(step_1_list_tag[i])
            
    for i in range(len(step_2_list)):
        rd = random.randint(1,10)
        if rd > 8:
            rd_picked = random.randint(0,len(did_list)-1)
            step_3_list.append(did_list[rd_picked] + '，' + step_2_list[i])
            tmp = []

            tmp += did_list_tag[rd_picked]
            tmp += ['O']
            tmp += step_2_list_tag[i]
            step_3_list_tag.append(tmp)
        else:
            step_3_list.append(step_2_list[i])
            step_3_list_tag.append(step_2_list_tag[i])


    for i in range(len(step_3_list)):
        rd = random.randint(1,10)
        if rd > 8:
            if '(0-5)' in step_3_list[i]:
                rd_picked = random.randint(0,len(jh_0_5_list)-1)
                step_4_list.append(jh_0_5_list[rd_picked] + '，' + step_3_list[i][5:])
                tmp = []

                tmp += jh_0_5_list_tag[rd_picked]
                tmp += ['O']
                tmp += step_3_list_tag[i]
                step_4_list_tag.append(tmp)
            elif '(5-25)' in step_3_list[i]:
                rd_picked = random.randint(0,len(jh_5_25_list)-1)
                step_4_list.append(jh_5_25_list[rd_picked] + '，' + step_3_list[i][6:])
                tmp = []

                tmp += jh_5_25_list_tag[rd_picked]
                tmp += ['O']
                tmp += step_3_list_tag[i]
                step_4_list_tag.append(tmp)
            elif '(25-55)' in step_3_list[i]:
                rd_picked = random.randint(0,len(jh_25_55_list)-1)
                step_4_list.append(jh_25_55_list[rd_picked] + '，' + step_3_list[i][7:])
                tmp = []

                tmp += jh_25_55_list_tag[rd_picked]
                tmp += ['O']
                tmp += step_3_list_tag[i]
                step_4_list_tag.append(tmp)
            elif '(55-80)' in step_3_list[i]:
                rd_picked = random.randint(0,len(jh_55_80_list)-1)
                step_4_list.append(jh_55_80_list[rd_picked] + '，' + step_3_list[i][7:])
                tmp = []

                tmp += jh_55_80_list_tag[rd_picked]
                tmp += ['O']
                tmp += step_3_list_tag[i]
                step_4_list_tag.append(tmp)
            else:
                rd_picked = random.randint(0,len(jh_list)-1)
                step_4_list.append(jh_list[rd_picked] + '，' + step_3_list[i])
                tmp = []

                tmp += jh_list_tag[rd_picked]
                tmp += ['O']
                tmp += step_3_list_tag[i]
                step_4_list_tag.append(tmp)
        else:
            step_4_list.append(step_3_list[i])
            step_4_list_tag.append(step_3_list_tag[i])


    for i in range(len(step_4_list)):
        rd = random.randint(1,10)
        if rd > 5:
            if '(0-5)' in step_4_list[i]:
                rd_picked = random.randint(0,len(sra_0_5_list)-1)
                step_5_list.append(sra_0_5_list[rd_picked][5:] + '，' + step_4_list[i][5:])
                tmp = []

                tmp += sra_0_5_list_tag[rd_picked]
                tmp += ['O']
                tmp += step_4_list_tag[i]
                step_5_list_tag.append(tmp)
            elif '(5-25)' in step_4_list[i]:
                rd_picked = random.randint(0,len(sra_5_25_list)-1)
                step_5_list.append(sra_5_25_list[rd_picked][6:] + '，' + step_4_list[i][6:])
                tmp = []

                tmp += sra_5_25_list_tag[rd_picked]
                tmp += ['O']
                tmp += step_4_list_tag[i]
                step_5_list_tag.append(tmp)
            elif '(25-55)' in step_4_list[i]:
                rd_picked = random.randint(0,len(sra_25_55_list)-1)
                step_5_list.append(sra_25_55_list[rd_picked][7:] + '，' + step_4_list[i][7:])
                tmp = []

                tmp += sra_25_55_list_tag[rd_picked]
                tmp += ['O']
                tmp += step_4_list_tag[i]
                step_5_list_tag.append(tmp)
            elif '(55-80)' in step_4_list[i]:
                rd_picked = random.randint(0,len(sra_55_80_list)-1)
                
                step_5_list.append(sra_55_80_list[rd_picked][7:] + '，' + step_4_list[i][7:])
                tmp = []

                tmp += sra_55_80_list_tag[rd_picked]
                tmp += ['O']
                tmp += step_4_list_tag[i]
                step_5_list_tag.append(tmp)
            else:
                rd_picked = random.randint(0,len(sra_list)-1)
                step_5_list.append(sra_list[rd_picked][sra_list[rd_picked].index(')')+1:] + '，' + step_4_list[i])
                tmp = []

                tmp += sra_list_tag[rd_picked]
                tmp += ['O']
                tmp += step_4_list_tag[i]
                
                step_5_list_tag.append(tmp)
        else:
            step_5_list.append(step_4_list[i])
            step_5_list_tag.append(step_4_list_tag[i])

    for i in range(len(step_5_list)):
        if ')' in step_5_list[i]:
            step_5_list[i] = step_5_list[i][step_5_list[i].index(')')+1:]
    
    return step_5_list, step_5_list_tag, disease_list, symptom_list, drug_list
    # return [], [], [], [], []

def do_create_2hop(list1, list2, list1_tag, list2_tag):

    dataset_list = []
    sentence_list = []
    return_tag_list = []
    for i in range(10):
        '''
        print("*******************************************")
        print(list1)
        print(list2)
        print("*******************************************")
        '''
        sent1 = random.randint(0,len(list1)-1)
        sent2 = random.randint(0,len(list2)-1)
        if [sent1, sent2] not in dataset_list:
            sentence = list1[sent1] + list2[sent2]
            '''
            print('=======================================================')
            print(sent1)
            print(sent2)
            print('=======================================================')
            '''
            tag = list1_tag[sent1] + list2_tag[sent2]
            dataset_list.append([sent1, sent2])
            sentence_list.append(sentence)
            return_tag_list.append(tag)
            
            if len(sentence) != len(tag):
                
                print('=======================================================')
                print('list1:')
                print(list1)
                print(list1_tag)
                print('list2:')
                print(list2)
                print(list2_tag)
                print(sentence)
                print(tag)
                print('Q1:')
                print(len(list1))
                print(sent1)
                print(list1[sent1])
                print(list1_tag[sent1])
                print('Q2:')
                print(len(list2))
                print(sent2)
                print(list2[sent2])
                print(list2_tag[sent2])
                print('=======================================================')
                
        else:
            continue
    return sentence_list, return_tag_list

def do_create_3hop(list1,list2,list3,list1_tag,list2_tag,list3_tag):
   
    dataset_list = []
    sentence_list = []
    return_tag_list = []    
    for i in range(100):
        sent1 = random.randint(0,len(list1)-1)
        sent2 = random.randint(0,len(list2)-1)
        sent3 = random.randint(0,len(list3)-1)
        if [sent1, sent2,sent3] not in dataset_list:
            sentence = list1[sent1] + list2[sent2] + list3[sent3]
            tag = list1_tag[sent1] + list2_tag[sent2] + list3_tag[sent3]
            sentence_list.append(sentence)
            dataset_list.append([sent1, sent2,sent3])
            return_tag_list.append(tag)
            if len(sentence) != len(tag):
                
                print('=======================================================')
                print('list1:')
                print(list1)
                print(list1_tag)
                print('list2:')
                print(list2)
                print(list2_tag)
                print(sentence)
                print(tag)
                print('Q1:')
                print(len(list1))
                print(sent1)
                print(list1[sent1])
                print(list1_tag[sent1])
                print('Q2:')
                print(len(list2))
                print(sent2)
                print(list2[sent2])
                print(list2_tag[sent2])
                print('=======================================================')
        else:
            continue
    return sentence_list, return_tag_list

def create_file():
    Zhengduanguanxi_list, Zhengduanguanxi_list_tag, disease_list, symptom_list, drug_list = create_tag1_list()

    Bingfa_list = []
    Bingfa_list_tag = []
    with open('parts/parts_Bingfa/label_Bingfa_q.txt','r',encoding='utf-8') as infile:
        for line in infile:
            Bingfa_list.append(line[:-1])
    with open('parts/parts_Bingfa/label_Bingfa_q_tag.txt','r',encoding='utf-8') as infile:
        for line in infile:
            tmp = line[:-1].split(',')
            Bingfa_list_tag.append(tmp)
    

    for i,line2 in zip(range(len(Bingfa_list)), Bingfa_list_tag):
        if 'DIS' in Bingfa_list[i]:
            disease_rd = random.randint(0,len(disease_list)-1)
            have_dis = [have_dis.start() for have_dis in re.finditer('DIS', Bingfa_list[i])]
            if len(have_dis) != 0:
                Bingfa_list[i] = Bingfa_list[i].replace('DIS', disease_list[disease_rd])
                  
                cor = 0
                push = 0
                for j in range(len(have_dis)):
                    dis = []
                    for k in range(len(disease_list[disease_rd])-2):
                        dis += ['I-D']
                    dis = ['B-D'] + dis + ['E-D']
                    
                    line2[have_dis[j]-cor*3+push:have_dis[j]-cor*3+push+1] = iter(dis)
                    cor += 1
                    push += len(dis)

    
    Tuijiankeshi_list = []
    Tuijiankeshi_list_tag = []
    with open('parts/parts_Tuijiankeshi/label_Tuijiankeshi_q.txt','r',encoding='utf-8') as infile:
        for line in infile:
            Tuijiankeshi_list.append(line[:-1])
    with open('parts/parts_Tuijiankeshi/label_Tuijiankeshi_q_tag.txt','r',encoding='utf-8') as infile:
        for line in infile:
            tmp = line[:-1].split(',')
            Tuijiankeshi_list_tag.append(tmp)
    
    for i,line2 in zip(range(len(Tuijiankeshi_list)), Tuijiankeshi_list_tag):
        if 'DIS' in Tuijiankeshi_list[i]:
            disease_rd = random.randint(0,len(disease_list)-1)
            have_dis = [have_dis.start() for have_dis in re.finditer('DIS', Tuijiankeshi_list[i])]
            if len(have_dis) != 0:
                Tuijiankeshi_list[i] = Tuijiankeshi_list[i].replace('DIS', disease_list[disease_rd])
                  
                cor = 0
                push = 0
                for j in range(len(have_dis)):
                    dis = []
                    for k in range(len(disease_list[disease_rd])-2):
                        dis += ['I-D']
                    dis = ['B-D'] + dis + ['E-D']
                    
                    line2[have_dis[j]-cor*3+push:have_dis[j]-cor*3+push+1] = iter(dis)
                    cor += 1
                    push += len(dis)
        


    Peiwuguanxi_list = []
    Peiwuguanxi_list_tag = []
    with open('parts/parts_Peiwuguanxi/label_Peiwuguanxi_q.txt','r',encoding='utf-8') as infile:
        for line in infile:
            Peiwuguanxi_list.append(line[:-1])
    with open('parts/parts_Peiwuguanxi/label_Peiwuguanxi_q_tag.txt','r',encoding='utf-8') as infile:
        for line in infile:
            tmp = line[:-1].split(',')
            Peiwuguanxi_list_tag.append(tmp)
    
    for i,line2 in zip(range(len(Peiwuguanxi_list)), Peiwuguanxi_list_tag):
        if 'MED' in Peiwuguanxi_list[i]:
            drug_rd = random.randint(0,len(drug_list)-1)
            have_med = [have_med.start() for have_med in re.finditer('MED', Peiwuguanxi_list[i])]
            if len(have_med) != 0:
                Peiwuguanxi_list[i] = Peiwuguanxi_list[i].replace('MED', drug_list[drug_rd])
                  
                cor = 0
                push = 0
                for j in range(len(have_med)):
                    med = []
                    for k in range(len(drug_list[drug_rd])-2):
                        med += ['I-M']
                    med = ['B-M'] + med + ['E-M']
                    
                    line2[have_med[j]-cor*3+push:have_med[j]-cor*3+push+1] = iter(med)
                    cor += 1
                    push += len(med)
    
    
    Fashengbuwei_list = []
    Fashengbuwei_list_tag = []
    with open('parts/parts_Fashengbuwei/label_Fashengbuwei_q.txt','r',encoding='utf-8') as infile:
        i = 0
        for line in infile:
            if i == 0:
                Fashengbuwei_list.append(line[1:-1])
                i += 1
            else:
               
                Fashengbuwei_list.append(line[:-1])
    with open('parts/parts_Fashengbuwei/label_Fashengbuwei_q_tag.txt','r',encoding='utf-8') as infile:
        i = 0
        for line in infile:
            
            if i == 0:
                tmp = line[1:-1].split(',')
                Fashengbuwei_list_tag.append(tmp)
                i+= 1
            else:
                tmp = line[:-1].split(',')
                Fashengbuwei_list_tag.append(tmp)

    for i,line2 in zip(range(len(Fashengbuwei_list)), Fashengbuwei_list_tag):
        if 'DIS' in Fashengbuwei_list[i]:
            disease_rd = random.randint(0,len(disease_list)-1)
            have_dis = [have_dis.start() for have_dis in re.finditer('DIS', Fashengbuwei_list[i])]
            if len(have_dis) != 0:
                Fashengbuwei_list[i] = Fashengbuwei_list[i].replace('DIS', disease_list[disease_rd])
                  
                cor = 0
                push = 0
                for j in range(len(have_dis)):
                    dis = []
                    for k in range(len(disease_list[disease_rd])-2):
                        dis += ['I-D']
                    dis = ['B-D'] + dis + ['E-D']
                    
                    line2[have_dis[j]-cor*3+push:have_dis[j]-cor*3+push+1] = iter(dis)
                    cor += 1
                    push += len(dis)
    



    Jinjizheng_list = []
    Jinjizheng_list_tag = []
    with open('parts/parts_Jinjizheng/label_Jinjizheng_q.txt','r',encoding='utf-8') as infile:
        for line in infile:
            Jinjizheng_list.append(line[:-1])
    with open('parts/parts_Jinjizheng/label_Jinjizheng_q_tag.txt','r',encoding='utf-8') as infile:
        for line in infile:
            tmp = line[:-1].split(',')
            Jinjizheng_list_tag.append(tmp)

    for i,line2 in zip(range(len(Jinjizheng_list)), Jinjizheng_list_tag):
        if 'DIS' in Jinjizheng_list[i]:
            disease_rd = random.randint(0,len(disease_list)-1)
            have_dis = [have_dis.start() for have_dis in re.finditer('DIS', Jinjizheng_list[i])]
            if len(have_dis) != 0:
                Jinjizheng_list[i] = Jinjizheng_list[i].replace('DIS', disease_list[disease_rd])
                  
                cor = 0
                push = 0
                for j in range(len(have_dis)):
                    dis = []
                    for k in range(len(disease_list[disease_rd])-2):
                        dis += ['I-D']
                    dis = ['B-D'] + dis + ['E-D']
                    
                    line2[have_dis[j]-cor*3+push:have_dis[j]-cor*3+push+1] = iter(dis)
                    cor += 1
                    push += len(dis)
    for i,line2 in zip(range(len(Jinjizheng_list)), Jinjizheng_list_tag):
        if 'MED' in Jinjizheng_list[i]:
            drug_rd = random.randint(0,len(drug_list)-1)
            have_med = [have_med.start() for have_med in re.finditer('MED', Jinjizheng_list[i])]
            if len(have_med) != 0:
                Jinjizheng_list[i] = Jinjizheng_list[i].replace('MED', drug_list[drug_rd])
                  
                cor = 0
                push = 0
                for j in range(len(have_med)):
                    med = []
                    for k in range(len(drug_list[drug_rd])-2):
                        med += ['I-M']
                    med = ['B-M'] + med + ['E-M']
                    
                    line2[have_med[j]-cor*3+push:have_med[j]-cor*3+push+1] = iter(med)
                    cor += 1
                    push += len(med)
    




    
    Buliangfanying_list = []
    Buliangfanying_list_tag = []
    with open('parts/parts_Buliangfanying/label_Buliangfanying_q.txt','r',encoding='utf-8') as infile:
        for line in infile:
            Buliangfanying_list.append(line[:-1])
    with open('parts/parts_Buliangfanying/label_Buliangfanying_q_tag.txt','r',encoding='utf-8') as infile:
        for line in infile:
            tmp = line[:-1].split(',')
            Buliangfanying_list_tag.append(tmp)
    
    for i,line2 in zip(range(len(Buliangfanying_list)), Buliangfanying_list_tag):
        if 'MED' in Buliangfanying_list[i]:
            drug_rd = random.randint(0,len(drug_list)-1)
            have_med = [have_med.start() for have_med in re.finditer('MED', Buliangfanying_list[i])]
            if len(have_med) != 0:
                Buliangfanying_list[i] = Buliangfanying_list[i].replace('MED', drug_list[drug_rd])
                  
                cor = 0
                push = 0
                for j in range(len(have_med)):
                    med = []
                    for k in range(len(drug_list[drug_rd])-2):
                        med += ['I-M']
                    med = ['B-M'] + med + ['E-M']
                    
                    line2[have_med[j]-cor*3+push:have_med[j]-cor*3+push+1] = iter(med)
                    cor += 1
                    push += len(med)
    for i,line2 in zip(range(len(Buliangfanying_list)), Buliangfanying_list_tag):
        if 'SPT' in Buliangfanying_list[i]:
            spt_rd = random.randint(0,len(symptom_list)-1)
            have_spt = [have_spt.start() for have_spt in re.finditer('SPT', Buliangfanying_list[i])]
            if len(have_spt) != 0:
                Buliangfanying_list[i] = Buliangfanying_list[i].replace('SPT', symptom_list[spt_rd])
                  
                cor = 0
                push = 0
                for j in range(len(have_spt)):
                    spt = []
                    for k in range(len(symptom_list[spt_rd])-2):
                        spt += ['I-S']
                    spt = ['B-S'] + spt + ['E-S']
                    
                    line2[have_spt[j]-cor*3+push:have_spt[j]-cor*3+push+1] = iter(spt)
                    cor += 1
                    push += len(spt)
    


    Huanbingqingxiang_list = []
    Huanbingqingxiang_list_tag = []
    with open('parts/parts_Huanbingqingxiang/label_Huanbingqingxiang_q.txt','r',encoding='utf-8') as infile:
        i = 0
        for line in infile:
            if i == 0:
                Huanbingqingxiang_list.append(line[1:-1])
                i += 1
            else:
               
                Huanbingqingxiang_list.append(line[:-1])
    with open('parts/parts_Huanbingqingxiang/label_Huanbingqingxiang_q_tag.txt','r',encoding='utf-8') as infile:
        
        for line in infile:
            tmp = line[:-1].split(',')
            Huanbingqingxiang_list_tag.append(tmp)
    
    for i,line2 in zip(range(len(Huanbingqingxiang_list)), Huanbingqingxiang_list_tag):
        if 'DIS' in Huanbingqingxiang_list[i]:
            disease_rd = random.randint(0,len(disease_list)-1)
            have_dis = [have_dis.start() for have_dis in re.finditer('DIS', Huanbingqingxiang_list[i])]
            if len(have_dis) != 0:
                Huanbingqingxiang_list[i] = Huanbingqingxiang_list[i].replace('DIS', disease_list[disease_rd])
                  
                cor = 0
                push = 0
                for j in range(len(have_dis)):
                    dis = []
                    for k in range(len(disease_list[disease_rd])-2):
                        dis += ['I-D']
                    dis = ['B-D'] + dis + ['E-D']
                    
                    line2[have_dis[j]-cor*3+push:have_dis[j]-cor*3+push+1] = iter(dis)
                    cor += 1
                    push += len(dis)
    






    Jibingfenqi_list = []
    Jibingfenqi_list_tag = []
    with open('parts/parts_Jibingfenqi/label_Jibingfenqi_q.txt','r',encoding='utf-8') as infile:
        for line in infile:
            Jibingfenqi_list.append(line[:-1])
    with open('parts/parts_Jibingfenqi/label_Jibingfenqi_q_tag.txt','r',encoding='utf-8') as infile:
        for line in infile:
            tmp = line[:-1].split(',')
            Jibingfenqi_list_tag.append(tmp)

    for i,line2 in zip(range(len(Jibingfenqi_list)), Jibingfenqi_list_tag):
        if 'DIS' in Jibingfenqi_list[i]:
            disease_rd = random.randint(0,len(disease_list)-1)
            have_dis = [have_dis.start() for have_dis in re.finditer('DIS', Jibingfenqi_list[i])]
            if len(have_dis) != 0:
                Jibingfenqi_list[i] = Jibingfenqi_list[i].replace('DIS', disease_list[disease_rd])
                  
                cor = 0
                push = 0
                for j in range(len(have_dis)):
                    dis = []
                    for k in range(len(disease_list[disease_rd])-2):
                        dis += ['I-D']
                    dis = ['B-D'] + dis + ['E-D']
                    
                    line2[have_dis[j]-cor*3+push:have_dis[j]-cor*3+push+1] = iter(dis)
                    cor += 1
                    push += len(dis)
    
    for i,line2 in zip(range(len(Jibingfenqi_list)), Jibingfenqi_list_tag):
        if 'SPT' in Jibingfenqi_list[i]:
            spt_rd = random.randint(0,len(symptom_list)-1)
            have_spt = [have_spt.start() for have_spt in re.finditer('SPT', Jibingfenqi_list[i])]
            if len(have_spt) != 0:
                Jibingfenqi_list[i] = Jibingfenqi_list[i].replace('SPT', symptom_list[spt_rd])
                  
                cor = 0
                push = 0
                for j in range(len(have_spt)):
                    spt = []
                    for k in range(len(symptom_list[spt_rd])-2):
                        spt += ['I-S']
                    spt = ['B-S'] + spt + ['E-S']
                    
                    line2[have_spt[j]-cor*3+push:have_spt[j]-cor*3+push+1] = iter(spt)
                    cor += 1
                    push += len(spt)
    


    
    Linchuangbiaoxian_list = []
    Linchuangbiaoxian_list_tag = []
    with open('parts/parts_Linchuangbiaoxian/label_Linchuangbiaoxian_q.txt','r',encoding='utf-8') as infile:
        for line in infile:
            Linchuangbiaoxian_list.append(line[:-1])
    with open('parts/parts_Linchuangbiaoxian/label_Linchuangbiaoxian_q_tag.txt','r',encoding='utf-8') as infile:
        for line in infile:
            tmp = line[:-1].split(',')
            Linchuangbiaoxian_list_tag.append(tmp)

    for i,line2 in zip(range(len(Linchuangbiaoxian_list)), Linchuangbiaoxian_list_tag):
        if 'DIS' in Linchuangbiaoxian_list[i]:
            disease_rd = random.randint(0,len(disease_list)-1)
            have_dis = [have_dis.start() for have_dis in re.finditer('DIS', Linchuangbiaoxian_list[i])]
            if len(have_dis) != 0:
                Linchuangbiaoxian_list[i] = Linchuangbiaoxian_list[i].replace('DIS', disease_list[disease_rd])
                  
                cor = 0
                push = 0
                for j in range(len(have_dis)):
                    dis = []
                    for k in range(len(disease_list[disease_rd])-2):
                        dis += ['I-D']
                    dis = ['B-D'] + dis + ['E-D']
                    
                    line2[have_dis[j]-cor*3+push:have_dis[j]-cor*3+push+1] = iter(dis)
                    cor += 1
                    push += len(dis)
    
    for i,line2 in zip(range(len(Linchuangbiaoxian_list)), Linchuangbiaoxian_list_tag):
        if 'SPT' in Linchuangbiaoxian_list[i]:
            spt_rd = random.randint(0,len(symptom_list)-1)
            have_spt = [have_spt.start() for have_spt in re.finditer('SPT', Linchuangbiaoxian_list[i])]
            if len(have_spt) != 0:
                Linchuangbiaoxian_list[i] = Linchuangbiaoxian_list[i].replace('SPT', symptom_list[spt_rd])
                  
                cor = 0
                push = 0
                for j in range(len(have_spt)):
                    spt = []
                    for k in range(len(symptom_list[spt_rd])-2):
                        spt += ['I-S']
                    spt = ['B-S'] + spt + ['E-S']
                    
                    line2[have_spt[j]-cor*3+push:have_spt[j]-cor*3+push+1] = iter(spt)
                    cor += 1
                    push += len(spt)
    
    




    Shiyingzheng_list = []
    Shiyingzheng_list_tag = []
    with open('parts/parts_Shiyingzheng/label_Shiyingzheng_q.txt','r',encoding='utf-8') as infile:
        for line in infile:
            Shiyingzheng_list.append(line[:-1])
    with open('parts/parts_Shiyingzheng/label_Shiyingzheng_q_tag.txt','r',encoding='utf-8') as infile:
        for line in infile:
            tmp = line[:-1].split(',')
            Shiyingzheng_list_tag.append(tmp)

    for i,line2 in zip(range(len(Shiyingzheng_list)), Shiyingzheng_list_tag):
        if 'DIS' in Shiyingzheng_list[i]:
            disease_rd = random.randint(0,len(disease_list)-1)
            have_dis = [have_dis.start() for have_dis in re.finditer('DIS', Shiyingzheng_list[i])]
            if len(have_dis) != 0:
                Shiyingzheng_list[i] = Shiyingzheng_list[i].replace('DIS', disease_list[disease_rd])
                  
                cor = 0
                push = 0
                for j in range(len(have_dis)):
                    dis = []
                    for k in range(len(disease_list[disease_rd])-2):
                        dis += ['I-D']
                    dis = ['B-D'] + dis + ['E-D']
                    
                    line2[have_dis[j]-cor*3+push:have_dis[j]-cor*3+push+1] = iter(dis)
                    cor += 1
                    push += len(dis)
    
    for i,line2 in zip(range(len(Shiyingzheng_list)), Shiyingzheng_list_tag):
        if 'SPT' in Shiyingzheng_list[i]:
            spt_rd = random.randint(0,len(symptom_list)-1)
            have_spt = [have_spt.start() for have_spt in re.finditer('SPT', Shiyingzheng_list[i])]
            if len(have_spt) != 0:
                Shiyingzheng_list[i] = Shiyingzheng_list[i].replace('SPT', symptom_list[spt_rd])
                  
                cor = 0
                push = 0
                for j in range(len(have_spt)):
                    spt = []
                    for k in range(len(symptom_list[spt_rd])-2):
                        spt += ['I-S']
                    spt = ['B-S'] + spt + ['E-S']
                    
                    line2[have_spt[j]-cor*3+push:have_spt[j]-cor*3+push+1] = iter(spt)
                    cor += 1
                    push += len(spt)
    
    for i,line2 in zip(range(len(Shiyingzheng_list)), Shiyingzheng_list_tag):
        if 'MED' in Shiyingzheng_list[i]:
            drug_rd = random.randint(0,len(drug_list)-1)
            have_med = [have_med.start() for have_med in re.finditer('MED', Shiyingzheng_list[i])]
            if len(have_med) != 0:
                Shiyingzheng_list[i] = Shiyingzheng_list[i].replace('MED', drug_list[drug_rd])
                  
                cor = 0
                push = 0
                for j in range(len(have_med)):
                    med = []
                    for k in range(len(drug_list[drug_rd])-2):
                        med += ['I-M']
                    med = ['B-M'] + med + ['E-M']
                    
                    line2[have_med[j]-cor*3+push:have_med[j]-cor*3+push+1] = iter(med)
                    cor += 1
                    push += len(med)



    dataset = []
    label = []

    label_vec = [Zhengduanguanxi_list, Bingfa_list, Tuijiankeshi_list, Peiwuguanxi_list, Fashengbuwei_list, Jinjizheng_list, Buliangfanying_list, Huanbingqingxiang_list, Jibingfenqi_list, Linchuangbiaoxian_list,Shiyingzheng_list]

    label_vec_tag = [Zhengduanguanxi_list_tag, Bingfa_list_tag, Tuijiankeshi_list_tag, Peiwuguanxi_list_tag, Fashengbuwei_list_tag, Jinjizheng_list_tag, Buliangfanying_list_tag, Huanbingqingxiang_list_tag, Jibingfenqi_list_tag, Linchuangbiaoxian_list_tag,Shiyingzheng_list_tag]
    
    # 2-hop
    for i in range(150):
        for j in range(11-i-1):
            if i != 11-j-2:
                s,l = do_create_2hop(label_vec[i], label_vec[11-j-2], label_vec_tag[i], label_vec_tag[11-j-2])
                dataset += s
                label += l
                s,l = do_create_2hop(label_vec[11-j-2], label_vec[i], label_vec_tag[11-j-2], label_vec_tag[i])
                dataset += s
                label += l

            
    
    # 1-hop
    for i in range(11):
        for j in range(len(label_vec[i])):
            dataset.append(label_vec[i][j])
            
            label.append(label_vec_tag[i][j])
    
    # 3-hop
    for i in range(9):
        for j in range(11-i-1):
            for k in range(11-i-j-2):

                s,l = do_create_3hop(label_vec[i], label_vec[11-j-1], label_vec[11-j-k-2], label_vec_tag[i], label_vec_tag[11-j-1], label_vec_tag[11-j-k-2])
                dataset += s
                label += l
                s,l = do_create_3hop(label_vec[i], label_vec[11-j-k-2], label_vec[11-j-1], label_vec_tag[i], label_vec_tag[11-j-k-2], label_vec_tag[11-j-1])
                dataset += s
                label += l
                s,l = do_create_3hop(label_vec[11-j-1], label_vec[i], label_vec[11-j-k-2], label_vec_tag[11-j-1], label_vec_tag[i], label_vec_tag[11-j-k-2])
                dataset += s
                label += l
                s,l = do_create_3hop(label_vec[11-j-1], label_vec[11-j-k-2], label_vec[i], label_vec_tag[11-j-1], label_vec_tag[11-j-k-2], label_vec_tag[i])
                dataset += s
                label += l
                s,l = do_create_3hop(label_vec[11-j-k-2], label_vec[i], label_vec[11-j-1], label_vec_tag[11-j-k-2], label_vec_tag[i], label_vec_tag[11-j-1])
                dataset += s
                label += l

                s,l = do_create_3hop(label_vec[11-j-k-2], label_vec[11-j-1], label_vec[i], label_vec_tag[11-j-k-2], label_vec_tag[11-j-1], label_vec_tag[i])
                dataset += s
                label += l

                s,l = do_create_3hop(label_vec[i], label_vec[11-j-1], label_vec[11-j-k-2], label_vec_tag[i], label_vec_tag[11-j-1], label_vec_tag[11-j-k-2])
                dataset += s
                label += l
    
    
    li=list(range(len(dataset)))  
    random.shuffle(li)  
    
    dataset = [x for _,x in sorted(zip(li,dataset))]
    label = [x for _,x in sorted(zip(li,label))]

    label_str = []
    for i in label:
        tmp_label = ''
        for j in i:
            # print(j)
            tmp_label = tmp_label + j + ','
        label_str.append(tmp_label[:-1])
    #print(dataset)
    #print(label_str)
    with open('Entity_test.txt', 'w', encoding='utf-8') as outfile:
        for line in dataset[0:10000]:
            outfile.write(line+'\n')
        
    outfile.close()
    
    with open('Entity_test_label.txt', 'w', encoding='utf-8') as outfile:
        for line in label_str[0:10000]:
            outfile.write(''.join(e for e in line) + '\n')
    outfile.close()

    with open('Entity_val.txt', 'w', encoding='utf-8') as outfile:
        for line in dataset[10001:20000]:
            outfile.write(line+'\n')
        
    outfile.close()

    with open('Entity_val_label.txt', 'w', encoding='utf-8') as outfile:
        for line in label_str[10001:20000]:
            outfile.write(''.join(e for e in line) + '\n')
    outfile.close()

    with open('Entity_train.txt', 'w', encoding='utf-8') as outfile:
        for line in dataset[20001:]:
            outfile.write(line+'\n')
        
    outfile.close()

    with open('Entity_train_label.txt', 'w', encoding='utf-8') as outfile:
        for line in label_str[20001:]:
            outfile.write(''.join(e for e in line) + '\n')
    outfile.close()
    

def main():
    create_file()


if __name__ == '__main__':
    main()