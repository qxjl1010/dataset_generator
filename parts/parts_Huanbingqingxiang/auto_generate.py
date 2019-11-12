'''
= ['DIS，MED有用吗？','MED能有效果吗？','DIS吃什么药？','DIS应该用什么药物？','DIS要使用什么药膏？','DIS怎么用药？','大人能吃MED退烧吗？','DIS该吃什么药？','DIS应该吃什么药','MED可以治愈DIS吗？','DIS应该吃MED吗？','DIS，每天应该吃几片MED？','MED每天吃几片？','IDS，MED每餐吃几粒？','DIS睡前吃MED要吃几片？','得了DIS，早起要吃几片MED？','DIS睡前要喝多少MED？','MED要吃多久的药？']
l2 = []
for i in range(len(l)):
    l[i] = l[i].replace('DIS','O')
    l[i] = l[i].replace('MED','O')
    l[i] = l[i].replace('SPT','O')
    tmp_str = ''
    for j in range(len(l[i])):
        tmp_str += 'O,'
    l2.append(tmp_str[:-1])

print(l2)
'''
s = []
with open('label_Huanbingqingxiang_q.txt','r',encoding='utf-8') as infile:
    for line in infile:

        s = line.split('\',\'')

with open('label_Huanbingqingxiang_q.txt','w',encoding='utf-8') as outfile:
    for line in s:
        outfile.write(line + '\n')



with open('label_Huanbingqingxiang_q_tag.txt','w',encoding='utf-8') as outfile:
    for line in s:
        line = line.replace('DIS','O')
        line = line.replace('MED','O')
        line = line.replace('SPT','O')
        tag = ''
        for i in range(len(line)):
            tag += 'O,'
        outfile.write(tag[:-1]+'\n')