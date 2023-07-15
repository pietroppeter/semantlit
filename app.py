import streamlit as st
from gensim.models import KeyedVectors

model = KeyedVectors.load("./word2vec/word2vec.wordvectors", mmap='r')

SECRET_WORD = "poesia"
if "guesses" in st.session_state:
    guesses = st.session_state["guesses"]
else: 
    guesses = []


guess = st.text_input(label="Guess",value="")
if guess:
    guesses.append(guess)
    st.session_state["guesses"] = guesses
    for g in guesses:
        st.write(g)
        similarity = model.similarity(g, SECRET_WORD)
        st.write(similarity)



