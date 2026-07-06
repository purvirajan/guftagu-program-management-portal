import streamlit as st
from database import run_query, load_sql

st.set_page_config(
    page_title="Guftagu Student Directory",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Guftagu Student Directory")

query = load_sql("student_directory.sql")

directory = run_query(query)

st.subheader("Student Directory")

st.dataframe(
    directory,
    use_container_width=True,
    hide_index=True
)