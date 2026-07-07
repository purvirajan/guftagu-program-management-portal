import streamlit as st

st.set_page_config(
    page_title="Guftagu Progress Portal",
    page_icon="📚",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Page title */
h1 {
    color: #2C5282;
    font-size: 2.5rem;
    font-weight: 700;
}

/* Metric cards */
[data-testid="stMetric"] {
    background: linear-gradient(135deg, #E8F1FD, #FFFFFF);
    border-left: 6px solid #4285F4;
    padding: 1rem;
    border-radius: 14px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.08);
}

/* Buttons */
.stButton > button {
    width: 100%;
    background-color: #4285F4;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #2C5282;
}
</style>
""", unsafe_allow_html=True)

st.title("Guftagu Progress Portal")

st.write(
    "A centralized tool for viewing Guftagu mentee attendance, assessments, and progress."
)

st.page_link("pages/1_Student_Directory.py", label="Go to Student Directory")