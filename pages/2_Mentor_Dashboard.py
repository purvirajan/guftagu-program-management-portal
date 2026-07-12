import streamlit as st
from styles import load_css
from auth import require_login, logout_button

st.set_page_config(page_title="Mentor Dashboard", page_icon="👩‍🏫", layout="wide")

load_css()
require_login()
logout_button()

st.title("Mentor Dashboard")

st.write("Current mentees will appear here.")