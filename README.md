# semantlit

semantle in italian with streamlit

[semantle](https://semantle.com/) is a daily word game (like wordle) where you are trying to guess a word in a big vocabulary using as hints distances
from the target world computed using word2vec [embeddings](https://vickiboykis.com/what_are_embeddings/).
Another implementation of semantle in French: https://www.dictaly.com/semantiques/2dcaf4d2b31c

You can play a very minimal version in Italian of this game here: : https://semantlit.streamlit.app

_Warning_: it is an extremely frustrating game.

This version is just a small PoC created in a single morning at
[![Open Source Saturday](https://img.shields.io/badge/%E2%9D%A4%EF%B8%8F-open%20source%20saturday-F64060.svg)](https://www.meetup.com/it-IT/Open-Source-Saturday-Milano/) session
with [@czephyr](https://github.com/czephyr)

The goal was to implement the miminal set of features to make the goal playable.
In particular we are missing (call it a roadmap if you want):
- a daily set of words (we have a single word to guess)
- better explanations about the game (and documentation for the implementation)
- an improved interface (check the other versions in English and French linked above to get an idea what an interface could be)

## word2vec in Italian

https://huggingface.co/osiria/word2vec-light-uncased-it

download word2vec.wordvectors and word2vec.wordvectors.vectors.npy in `word2vec` folder

