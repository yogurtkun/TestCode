import re
import os

#3.5思路总结，reference误识别率高，下一步改进的方法有两个
#1. 交集中的元素找在title和ref中的位置，去掉多次重复的之后，求平均距离，不能超过一个数值
#2. 用已经确定的作者信息去交叉验证

global ref_dict
ref_dict = {}

#提取reference部分
abstract_s = r'@@@@@(?:R|r)eferences(.*?)$'
abstract_pattern = re.compile(abstract_s,re.S)

# 根据交集中单词的顺序来确定是否是同一个文章，效果比较差，会把正确的也排除，所以不使用
# def compare_seq(title,ref,subset):
#     print("@@@@@@@@@")
#     print(title)
#     print(ref)
#     print(subset)
#
#     title_seq = list(map(lambda x:(title.index(x),x),subset))
#     title_seq.sort(key= lambda x:x[0])
#     print(title_seq)
#     title_seq = list(map(lambda x:x[1],title_seq))
#
#     global pre
#     pre = 0
#     for item in title_seq:
#         if item in ref[pre:]:
#             pre = ref.index(item)
#         else:
#             return False
#
#     return True


#建立起来文章字典
def build_dict(filename):
    with open (filename,'r') as file:
        read_file = file.read()
        result = extract_pattern.findall(read_file)
    for item in result:
        ref_dict[item[0]] = (item[1],item[2])

#判断名字在附近行么
def future_judge(author_string,word_set):
    author_set = author_string.lower()
    author_set = re.split(' |;',author_set)
    author_set = set(author_set)

    # if 'Chris' in author_string:
    #     print(author_set)
    #     print(word_set)

    if '' in author_set:
        author_set.remove('')

    authot_list = author_string.split(';')
    if '' in authot_list:
        authot_list.remove('')
    author_num = len(authot_list)

    count = 0
    for word in author_set:
        if word in word_set:
            count += 1


    if count/author_num > 0.25:
        return True
    else:
        return False


#查找文章有哪些acl会议
def find_ref(filename):

    #打开的会议记录下来
    file_num = re.findall('(.*?).txt',filename)[0]
    map_file.write(file_num + '@@@@@')

    #打开文件，读取内容
    file_path = os.path.join('./lin_txt_processed',filename)
    with open(file_path,'rb') as file:
        read_file = file.read().decode('utf-8',errors='ignore')

    #提取出references部分
    abstract_part = abstract_pattern.findall(read_file)
    if len(abstract_part) == 0:
        map_file.write('\n')
        warning_file.write('no refer part:'+file_num+'\n')
        return []
    abstract_file = abstract_part[0].split('\n')

    #将references部分每行做成一个词的集合
    raw_text = []
    for id in range(len(abstract_file)):
        line = abstract_file[id]
        if line[-2] == ',' and id!= len(abstract_file):
            print(''.join(line,abstract_file[id+1]))

        temp_string = line.lower()
        temp_string = re.split(' |[,.:;]',temp_string)
        raw_text.append(temp_string)
    if len(raw_text) < 2:
        return []

    raw_text = list(map(lambda x:(set(x),x),raw_text))

    #取出所有的已在词典中的文献
    acl_ref_list = []
    for key,value in ref_dict.items():
        string = value[0]
        string = string.lower()
        string = re.split(' |[,.;:]',string)
        if len(string) < 4:
            continue
        set_string = set(string)
        if '' in set_string:
            set_string.remove('')


        for item in raw_text:
            mutual = item[0] & set_string
            #如果相似的词的数量超过标准标题的80%即可认为是出现了的
            if len(mutual)/len(set_string) > 0.80:
                # if 'J89-4002' == key:
                #     print(item[0])
                #     print(set_string)
                #     print(mutual)
                if future_judge(value[1],item[0]):
                    acl_ref_list.append(key)
                break


    if len(acl_ref_list) == 0:
        map_file.write('\n')
        warning_file.write('no ref'+file_num+'\n')
        return []

    for ref in acl_ref_list:
        map_file.write(ref+'; ')
    map_file.write('\n')

    return acl_ref_list



extract_string = '([A-Z]\d{2}-\d{4}):(.*?)@@@@@(.*?)\n'
extract_pattern = re.compile(extract_string)
warning_file = open('./no_references.txt','w')
map_file = open('./map_file.txt','w')

build_dict('./titleset.txt')

for parent,dirnames,filenames in os.walk('./lin_txt_processed'):
    for filename in filenames:
        print('try '+filename)
        ref_list = find_ref('W94-0307.txt')
        print('finish '+filename)
        break


warning_file.close()
map_file.close()