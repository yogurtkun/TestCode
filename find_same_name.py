#-*-coding:utf-8-*-
import re

author_dict = {}

def addToDict(name,title):
    if not name in author_dict:
        author_dict[name] = [title]
    else:
        author_dict[name].append(title)

with open('./titleset.txt','r') as file:
    read_file = file.read()

name_pair = re.findall('([A-Z]\d{2}-\d{4}).*?@@@@@(.*?)\n',read_file)

dst_file = open('./paper_author.txt','w')
for pair in name_pair:
    name_list = re.split('; |;',pair[1])
    for name in name_list:
        if name == '':
            continue
        addToDict(name,pair[0])

for key,value in author_dict.items():
    dst_file.write(key+':')
    for id in value:
        dst_file.write(id+';')
    dst_file.write('\n')

dst_file.close()