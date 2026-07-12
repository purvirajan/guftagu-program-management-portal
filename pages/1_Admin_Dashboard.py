import streamlit as st
from styles import load_css
from auth import require_login, logout_button

st.set_page_config(page_title="Admin Dashboard", page_icon="⚙️", layout="wide")

load_css()
require_login()
logout_button()

st.title("Admin Dashboard")

st.write("Program overview and administrative tools will go here.")

st.page_link("pages/1_Student_Directory.py", label="Student Directory", icon="👥")
st.page_link("pages/6_Assessment_Framework.py", label="Assessment Framework", icon="📋")