import json

'''
将文章和它引用的文章dict转化为文章和应用它的文章dict
'''

reverse_id_dict = {}

with open('../un_mod_mat/new_id_ref.txt','r') as file:
    read_file = file.read()
    id_ref_dict = json.load(read_file)