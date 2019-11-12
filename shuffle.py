import random

with open('auto_created_q.txt') as f:
    sentence1_list = [line.strip() for line in f]
f.close()

li=list(range(len(sentence1_list)))  
random.shuffle(li)  

with open('auto_created_l.txt') as f:
    label_list = [line.strip() for line in f]
f.close()

Z1 = [x for _,x in sorted(zip(li,sentence1_list))]
Z2 = [x for _,x in sorted(zip(li,label_list))]

thefile = open('auto_created_q.txt', 'w')
for item in Z1:
    thefile.write("%s\n" % item)
thefile.close()

thefile = open('auto_created_l.txt', 'w')
for item in Z2:
    thefile.write("%s\n" % item)
thefile.close()
