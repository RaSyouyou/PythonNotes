
#one-hot在Keras中的实现
from keras.preprocessing.text import Tokenizer

samples = [
    'i am ineavdable',
    'i am ironman',
    'i graduated from a college'
]


tokenizer = Tokenizer()
tokenizer.fit_on_texts(samples)

word_index = tokenizer.word_index

print(word_index)
print(len(word_index))

sequences = tokenizer.texts_to_sequences(samples)
print(sequences)

one_hot_results = tokenizer.texts_to_matrix(samples) #形成one-hot编码
print(one_hot_results)