import streamlit as st
import os.path
from gensim.models import KeyedVectors
from huggingface_hub import hf_hub_download

files = ["word2vec.wordvectors", "word2vec.wordvectors.vectors.npy"]

for file in files:
    if not os.path.exists(f"word2vec/{file}"):
        with st.spinner(f"Downloading {file}..."):
            hf_hub_download(
                repo_id="osiria/word2vec-light-uncased-it",
                filename=file,
                local_dir="word2vec",
                local_dir_use_symlinks=False,
            )

try:
    model = KeyedVectors.load("./word2vec/word2vec.wordvectors", mmap="r")
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


_ = st.text_input(label="Guess", value="", key="guess_input", on_change=submit)
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
