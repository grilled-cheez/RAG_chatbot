import streamlit as st
import tempfile


def upload_files():
    with st.sidebar:
        st.header("Upload PDFs ")
        upload_files = st.file_uploader(
            "Choose files", type="pdf", accept_multiple_files=True
        )
        submit = st.button("Submit to DB")
    return upload_files, submit


def save_uploaded(upload_files):
    file_paths = []
    for file in upload_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(file.read())
            file_paths.append(tmp.name)
    return file_paths
