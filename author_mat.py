import re

def clean_list(x):
    while '' in x:
        x.remove('')

#建立dict
def build_dict(id,a_list,dict):
    dict[id] = a_list
    return

log_file = open('./log_info.txt','w')

id_author_dict = {}
paper_ref_dict = {}
same_name_dict = {}
author_id_dict = {}
author_author_dict = {}

#建立起文章id对作者名的dict
with open('./titleset.txt','r') as file:
    read_file = file.read()

title_set_string = '([A-Z]\d{2}-\d{4}):.*?@@@@@(.*?)\n'
title_set_pattern = re.compile(title_set_string)

id_author_list = title_set_pattern.findall(read_file)
for pair in id_author_list:
    name_list = re.split('; |;',pair[1])
    clean_list(name_list)
    build_dict(pair[0],name_list,id_author_dict)

#建立id互相引用的dict
with open('./map_file.txt','r') as file:
    read_file = file.read()

map_file_string = '([A-Z]\d{2}-\d{4})@@@@@(.*?)\n'
map_file_pattern = re.compile(map_file_string)

paper_ref_list = map_file_pattern.findall(read_file)
for pair in paper_ref_list:
    ref_list = re.split('; ',pair[1])
    clean_list(ref_list)
    build_dict(pair[0],ref_list,paper_ref_dict)

#建立同名dict和author对paper的dict
with open('./paper_author.txt','r') as file:
    read_file = file.read()

author_paper_string = '(.*?):(.*?)@@@@@(.*?)\n'
author_paper_pattern = re.compile(author_paper_string)

author_info_list = author_paper_pattern.findall(read_file)
for item in author_info_list:
    paper_list = item[1].split(';')
    clean_list(paper_list)
    same_list = item[2].split(';')
    clean_list(same_list)
    for pair in same_list:
        build_dict(pair,item[0],same_name_dict)
    build_dict(item[0],paper_list,author_id_dict)

#建立起来author之间的互相引用关系
for name,paper in author_id_dict.items():
    pass

log_file.write(str(author_id_dict))

log_file.close()