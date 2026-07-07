import streamlit as st
from database import run_query, load_sql

st.set_page_config(
    page_title="Student Directory",
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

st.title("Student Directory")

query = load_sql("student_directory.sql")
directory = run_query(query)

col1, col2, col3 = st.columns(3)

with col1:
    search_term = st.text_input("Search Student Name")

with col2:
    assessment_filter = st.selectbox(
        "Last Assessment",
        ["All", "Beginner", "Not Assessed"]
    )

with col3:
    level_filter = st.selectbox(
        "English Level",
        ["All", "Beginner", "Intermediate", "Advanced"]
    )

if search_term:
    directory = directory[
        directory["Student"].str.contains(search_term, case=False, na=False)
    ]

if assessment_filter != "All":
    directory = directory[
        directory["Last Assessment"] == assessment_filter
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