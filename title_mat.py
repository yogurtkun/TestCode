import re

paper_list = []
paper_dict = {}

with open('./map_file.txt','r') as file:
    read_file = file.read()

ex_str = r'(.*?)@@@@@(.*?)\n'
ex_pattern = re.compile(ex_str)

global count
count = 0

pair = re.findall(ex_pattern,read_file)
dim = len(pair)
for item in pair:
    ref_list = re.split('[ ;]',item[1])
    while '' in ref_list:
        ref_list.remove('')
    while ' ' in ref_list:
        ref_list.remove(' ')
    new_pair = (item[0],ref_list)
    paper_list.append(new_pair)
    paper_dict[item[0]] = count
    count += 1

write_file = open('./title_mat.txt','w')
for item in paper_list:
    line = [0 for x in range(dim)]
    write_file.write(item[0]+' ')
    for ref in item[1]:
        if not ref in paper_dict:
            continue
        line[paper_dict[ref]] = 1
    line = list(map(lambda x:str(x),line))
    write_file.write(' '.join(line)+'\n')

write_file.close()