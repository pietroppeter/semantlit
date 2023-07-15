from gensim.models import KeyedVectors

model = KeyedVectors.load("./word2vec/word2vec.wordvectors", mmap='r')

model.most_similar("poesia", topn=5)
