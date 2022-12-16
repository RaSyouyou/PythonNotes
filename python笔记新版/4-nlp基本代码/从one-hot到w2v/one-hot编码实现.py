

#one-hot编码
import numpy as np

samples = [
    'i am ineavdable',
    'i am ironman',
    'i graduated from a college'
]

token_index = {}
for sample in samples:
    for word in sample.split():
        if word not in token_index:
            token_index[word] = len(token_index) +1#录入字典token_index

print(len(token_index))
print(token_index)

results = np.zeros(shape=(len(samples),
                          len(token_index) + 1,
                          max(token_index.values())+1
                          )
                   )#np.zeros 返回一个用零充满一个给定维度的矩阵

# print(results.shape)

for i,sample in enumerate(samples):
    for j,word in list(enumerate(sample.split())):
        index = token_index.get(word)
        results[i,j,index] = 1

print(results)

results = np.zeros(shape=(len(samples),max(token_index.values())+1))

for i ,sample in enumerate(samples):
    for _,word in list(enumerate(sample.split())):
        index = token_index.get(word)
        results[i,index] = 1

print(results)


