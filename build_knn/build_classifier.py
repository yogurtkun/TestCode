import json
import nltk
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
trans_table = {ord(c): None for c in string.punctuation}  #去掉标点符号的转换矩阵

#还原成词根
def stem_tokens(tokens,stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

#分词
def my_tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens,stemmer)
    return stems

log_file = open('./log.txt','w')
tfidf_vect = TfidfVectorizer(tokenizer= my_tokenize, stop_words='english')  #tfidf转换向量矩阵

#读取信息
with open('./info_list.trn','r') as file:
    read_file = file.read()

info_list = json.loads(read_file) #两级list[id,分类，文本]

class_id_list = list(map(lambda x:x[1],info_list)) #得到文章分类结果的list
text_list = list(map(lambda x:x[2].lower(),info_list))  #包含内容的list
text_no_punction = list(map(lambda x:x.translate(trans_table),text_list))  #文章内容去掉标点符号

tfidf_mat = tfidf_vect.fit_transform(text_no_punction)
print(type(tfidf_mat))

log_file.close()