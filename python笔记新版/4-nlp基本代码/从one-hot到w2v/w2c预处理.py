from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import re
import math
import random
import jieba
import numpy as np
from six.moves import xrange
import tensorflow as tf

#停用词
stop_words = []
with open('stopwords.txt','r',encoding = 'utf-8') as f_stopwords:
    for line in f_stopwords:
        line = line.replace('\r','').replace('\n','').strip()
        stop_words.append(line)


#预处理
raw_word_list = []
rules = u"([\u4e00-\u9fa5]+)"
pattern = re.compile(rules)
f_writer = open('处理完成的笑傲江湖.txt','w',encoding='utf-8')

with open('笑傲江湖.txt','r',encoding = 'utf-8') as f_reader:
    lines = f_reader.readlines()
    for line in lines :
        line = line.replace('\r','').replace('\n','').strip()  #去空格
        if line == '' or line is None:
            continue
        line = ' '.join(jieba.cut(line))
        seg_list = pattern.findall(line)
        word_list = []
        for word in seg_list:
            if word not in stop_words:
                word_list.append(word)
        if len(word_list) > 0 :
            raw_word_list.extend(word_list)
            line = ' '.join(seg_list)
            f_writer.write(line+'\n')
            f_writer.flush()

f_writer.close()

print(len(raw_word_list))
print(len(set(raw_word_list)))
vocabulary_size = len(set(raw_word_list))


words = raw_word_list
count = [['UNKNOW','-1']]
count.extend(collections.Counter(words).most_common(10))#most common 10th words
print(count)
