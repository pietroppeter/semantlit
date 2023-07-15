import streamlit as st
from gensim.models import KeyedVectors

try:
    model = KeyedVectors.load("./word2vec/word2vec.wordvectors", mmap='r')
except FileNotFoundError:
    st.error("Word2Vec file not found")

SECRET_WORD = "poesia"
if "guesses" in st.session_state:
    guesses = st.session_state.guesses
else: 
    guesses = []

if "guess" not in st.session_state:
    st.session_state.guess = ""

def submit():
    st.session_state.guess = st.session_state.guess_input
    st.session_state.guess_input = ""

_ = st.text_input(label="Guess",value="",key="guess_input",on_change=submit)
guess = st.session_state.guess
if guess:
    if guess in model.key_to_index:
        guesses.append(guess)
        st.session_state["guesses"] = guesses
    else:
        st.error("We don't have this word sorry")
    for g in guesses:
        st.write(g)
        similarity = model.similarity(g, SECRET_WORD)
        st.write(similarity)
