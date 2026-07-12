import streamlit as st
from database import run_query
from styles import load_css
from auth import require_login, logout_button

st.set_page_config(
    page_title="Student Dashboard",
    page_icon="🎓",
    layout="wide"
)

load_css()
require_login()

student_id = st.session_state.get("selected_student_id", 1)

student = run_query(f"""
SELECT
    student_name,
    native_language,
    english_level,
    date_enrolled
FROM students
WHERE student_id = {student_id};
""").iloc[0]

st.title(f"Welcome back, {student['student_name']}")

col1, col2 = st.columns([6, 1])

with col1:
    st.caption("🧪 Portfolio Demo")

with col2:
    logout_button()

attendance = run_query(f"""
SELECT
    COUNT(*) AS total_sessions,
    COUNT(*) FILTER (WHERE attended = true) AS attended_sessions
FROM sessions
WHERE student_id = {student_id};
""").iloc[0]

total_sessions = attendance["total_sessions"]
attended_sessions = attendance["attended_sessions"]

attendance_rate = round(
    100 * attended_sessions / total_sessions, 1
) if total_sessions > 0 else 0

mentor = run_query(f"""
SELECT m.mentor_name
FROM student_mentors sm
JOIN mentors m
    ON sm.mentor_id = m.mentor_id
WHERE sm.student_id = {student_id}
  AND sm.end_date IS NULL;
""")

latest_assessment = run_query(f"""
SELECT
    assessment_level,
    assessment_date
FROM assessments
WHERE student_id = {student_id}
ORDER BY assessment_date DESC
LIMIT 1;
""")


st.write(
    f"{student['english_level']} learner · Native language: {student['native_language']}"
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Attendance", f"{attendance_rate}%")

with col2:
    st.metric("Sessions Completed", f"{attended_sessions} / {total_sessions}")

with col3:
    st.metric("Current Level", student["english_level"])

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Current Mentor")

    if mentor.empty:
        st.info("No current mentor assigned.")
    else:
        st.write(mentor.iloc[0]["mentor_name"])

with col2:
    st.subheader("Latest Assessment")

    if latest_assessment.empty:
        st.info("No assessment recorded yet.")
    else:
        latest = latest_assessment.iloc[0]
        st.write(f"{latest['assessment_level']} Assessment")
        st.write(f"Completed on {latest['assessment_date']}")

st.divider()

if st.button("View My Full Profile"):
    st.switch_page("pages/2_Student_Profile.py")

st.page_link(
    "pages/6_Assessment_Framework.py",
    label="View Assessment Framework",
    icon="📋"
)