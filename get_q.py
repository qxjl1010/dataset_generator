
# -*- coding: utf-8 -*-   
  
import os  

txt_list = []

def get_file_name(path): 
    image_files = []
    for file in os.listdir(path):
        image_files.append(file)
    image_names = [os.path.splitext(name)[0] for name in image_files if os.path.splitext(name)[1]=='.txt']
    if len(image_names) >= 200:
        return []
    else:
        return image_names

def walkFile(file):
    global txt_list
    i = 0
    for root, dirs, files in os.walk(file):
        if i == 1:
            break
        i += 1
        j = 0
        for d in dirs:
            j += 1
            txt_list += get_file_name(os.path.join(root,d))


walkFile('D:\\scrapy\\qa\\output')

with open('tmp.txt', 'w', encoding='utf-8') as outfile:
    for line in txt_list:
        outfile.write(line)
        outfile.write('\n')
outfile.close()

