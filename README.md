# semantlit

[semantle](https://semantle.com/) in Italian with [streamlit](https://streamlit.io/).

Semantle (name taken from the English version linked above) is a daily word game (like wordle) where you are trying to guess a word in a big vocabulary using as hints distances
from the target word computed using word2vec [embeddings](https://vickiboykis.com/what_are_embeddings/).
Another implementation of semantle in French is called [Sémantique](https://www.dictaly.com/semantiques/2dcaf4d2b31c).
There is a version in German called [Semantel](https://semantel.tarphos.de/).

You can play a very minimal version in Italian of this game (deployed on streamlit cloud) here: https://semantlit.streamlit.app

_Warning_: it is an extremely frustrating game.

This version is just a small PoC created in a single morning at
[![Open Source Saturday](https://img.shields.io/badge/%E2%9D%A4%EF%B8%8F-open%20source%20saturday-F64060.svg)](https://www.meetup.com/it-IT/Open-Source-Saturday-Milano/)
in a session with [@czephyr](https://github.com/czephyr) (in the afternoon we worked on [NLP on MLP](https://github.com/czephyr/nlp_on_mlp/blob/master/notebooks/simple_relation.ipynb)).

The goal was to implement the minimal set of features to make the goal playable.
In particular we are missing (call it a roadmap if you want):
- a daily set of words (we have a single word to guess)
- better explanations about the game (and documentation for the implementation)
- an improved interface (check the other versions in English and French linked above to get an idea what an interface could be)

## word2vec in Italian

https://huggingface.co/osiria/word2vec-light-uncased-it

download word2vec.wordvectors and word2vec.wordvectors.vectors.npy in `word2vec` folder

