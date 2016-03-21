#-*-coding:utf-8-*-
import re
from compare_name import ifSameName
from compare_name import ifSameNameP

author_dict = {}

def addToDict(name,title):

    if name in author_dict:
        author_dict[name][0].append(title)
        return

    if re.search('^ *$',name):
        return

    for key in author_dict:
        if ifSameNameP(key,name):
            author_dict[key][0].append(title)
            if not name in author_dict[key][1]:
                author_dict[key][1].append(name)
            return

    author_dict[name] = ([title],[])

    # if not name in author_dict:
    #     author_dict[name] = [title]
    # else:
    #     author_dict[name].append(title)

with open('./titleset.txt','r') as file:
    read_file = file.read()

name_pair = re.findall('([A-Z]\d{2}-\d{4}).*?@@@@@(.*?) *\n',read_file)

dst_file = open('./paper_author.txt','w')
log_file = open('./log.txt','w')

for pair in name_pair:
    name_list = re.split('; |;',pair[1])
    for name in name_list:
        if name == '':
            continue
        addToDict(name,pair[0])
    print('Finish '+pair[0])

for key,value in author_dict.items():
    dst_file.write(key+':')
    for id in value[0]:
        dst_file.write(id+';')
    dst_file.write('@@@@@')
    for samename in value[1]:
        dst_file.write(samename+';')
    dst_file.write('\n')

    if len(value[1]) != 0:
        log_file.write(key+':')
        for id in value[0]:
            log_file.write(id+';')
        log_file.write('@@@@@')
        for samename in value[1]:
            log_file.write(samename+';')
        log_file.write('\n')


dst_file.close()
log_file.close()