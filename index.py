import streamlit as st
import warnings
import logging

from modules.pdfhandler import upload_files
from modules.vectorstore import load_vectorstore
from modules.chroma_inspector import inspect_chroma
from modules.chat import display_chat_history, download_chat_history, handle_user_input
from modules.llm import get_llm_chain

from dotenv import load_dotenv

warnings.filterwarnings("ignore")
logging.getLogger("transformers").setLevel(logging.ERROR)

st.set_page_config(page_title="Ragbot")

# application title

st.title("sup bey")

# pdfs upload

uploaded_files, submitted = upload_files()

load_dotenv()

# user submit to vectorstore

if submitted and upload_files:
    with st.spinner("Updating VectorDB"):
        vectorstore = load_vectorstore(uploaded_files)
        st.session_state.vectorstore = vectorstore


if "vectorstore" in st.session_state:
    inspect_chroma(st.session_state.vectorstore)

display_chat_history()


if "vectorstore" in st.session_state:
    handle_user_input(get_llm_chain(st.session_state.vectorstore))


# LLM chain


download_chat_history()
