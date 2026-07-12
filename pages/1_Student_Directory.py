import streamlit as st
from database import run_query, load_sql
from styles import load_css
st.set_page_config(
    page_title="Student Directory",
    page_icon="📚",
    layout="wide"
)

load_css()
from auth import require_login, logout_button

require_login()
logout_button()

st.title("Student Directory")

query = load_sql("student_directory.sql")
directory = run_query(query)

col1, col2 = st.columns([2,1])

with col1:
    search_term = st.text_input("Search Student Name")


with col2:
    level_filter = st.selectbox(
        "English Level",
        ["All", "Beginner", "Intermediate", "Advanced"]
    )

if search_term:
    directory = directory[
        directory["Student"].str.contains(search_term, case=False, na=False)
    ]



if level_filter != "All":
    directory = directory[
        directory["Level"] == level_filter
    ]

st.caption(f"Showing {len(directory)} mentees")

st.divider()

for index, row in directory.iterrows():
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns([3, 2, 2, 2])

        with col1:
            if st.button(
                row["Student"],
                key=f"student_{row['student_id']}"
            ):
                st.session_state["selected_student_id"] = row["student_id"]
                st.switch_page("pages/2_Student_Profile.py")

        with col2:
            st.write(f"**Level:** {row['Level']}")

        with col3:
            st.write(f"**Attendance:** {row['Attendance']}%")

        with col4:
            st.write(f"**Last Assessment:** {row['Last Assessment']}")