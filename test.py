import re
import os

abstract_s = r'(?:R|r)eferences(.*?)$'
abstract_pattern = re.compile(abstract_s,re.S)

def find_ref(filename):
    print(filename)
    file_path = os.path.join('./lin_txt_processed',filename)
    with open(file_path,'rb') as file:
        read_file = file.read().decode('utf-8',errors='ignore')

    abstract_part = abstract_pattern.findall(read_file)
    print(abstract_part)
    if len(abstract_part) == 0:
        return
    if '@@@@@' in abstract_part[0]:
        print('######'+filename)

for parent,dirnames,filenames in os.walk('./lin_txt_processed'):
    total_num = len(filenames)
    finish_num = 0
    for filename in filenames:
        if not re.match('[A-Z]\d{2}-\d{4}.txt',filename):
            continue
        if '000' in filename:
            continue
        ref_list = find_ref('W12-2004.txt')
        break
