import streamlit as st

def load_css():
    st.markdown("""
    <style>

    /* ---------- App ---------- */

    html, body, .stApp {
        background-color: #F6F5F2;
        color: #1F1F1F;
        font-family: "Times New Roman", Georgia, serif;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* ---------- Headings ---------- */

    h1, h2, h3 {
        color: #1F1F1F;
        font-family: "Times New Roman", Georgia, serif;
        font-weight: 600;
    }

    /* ---------- Metric Cards ---------- */

    [data-testid="stMetric"] {
        background-color: #DDE7DB;
        border-left: 5px solid #C97C5D;
        border-radius: 12px;
        padding: 0.8rem;
        box-shadow: none;
    }

    [data-testid="stMetricLabel"] {
        font-size: 0.9rem;
    }

    [data-testid="stMetricValue"] {
        font-size: 1.6rem;
    }

    /* ---------- Cards / Containers ---------- */

    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #DDE7DB;
        border: 1px solid #B7C8B2;
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 0.75rem;
    }

    /* ---------- Buttons ---------- */

    .stButton > button {
        width: auto;
        background-color: #C9D8C5;
        color: #1F1F1F;
        border: 1px solid #AEBFA9;
        border-radius: 8px;
        padding: 0.45rem 0.9rem;
        font-size: 0.9rem;
        font-weight: 600;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        background-color: #C97C5D;
        color: white;
        border-color: #C97C5D;
    }

    /* ---------- Homepage ---------- */

    .home-hero {
        text-align: center;
        padding-top: 5rem;
        padding-bottom: 2rem;
    }

    .home-hero h1 {
        font-size: 3rem;
        margin-bottom: 1rem;
    }

    .home-hero p {
        max-width: 700px;
        margin: 0 auto;
        line-height: 1.6;
        font-size: 1.15rem;
    }

    /* ---------- Assessment Framework ---------- */

    .framework-hero {
        background-color: #DDE7DB;
        border-left: 8px solid #C97C5D;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 2rem;
    }

    .framework-hero h3 {
        margin-bottom: 0.5rem;
    }

    .framework-hero p {
        margin-bottom: 0;
        line-height: 1.6;
    }
    .login-card {
    max-width: 520px;
    margin: 3rem auto 1.5rem auto;
    padding: 2rem;
    background-color: #DDE7DB;
    border-left: 6px solid #C97C5D;
    border-radius: 16px;
    text-align: center;
    }

    .login-card h2 {
        margin-bottom: 0.5rem;
    }

    .login-card p {
        margin-bottom: 0;
    }

    .login-note {
        text-align: center;
        margin-top: 1rem;
        color: #666;
    }

    </style>
    """, unsafe_allow_html=True)

    