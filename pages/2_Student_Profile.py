import streamlit as st
from database import run_query
from styles import load_css
import pandas as pd

st.set_page_config(
    page_title="Student Profile",
    page_icon="👤",
    layout="wide"
)

load_css()
from auth import require_login, logout_button, get_current_student_id
require_login()
logout_button()

user_id = st.session_state.get("user_id")
selected_role = st.session_state.get("selected_role")

if user_id is None:
    st.warning("Please log in from the homepage.")
    st.stop()

student_id = get_current_student_id()

student_info = run_query(f"""
SELECT
    student_name,
    native_language,
    english_level,
    date_enrolled
FROM students
WHERE student_id = {student_id};
""")

mentor_history = run_query(f"""
SELECT
    m.mentor_name,
    sm.start_date,
    sm.end_date,
    CONCAT(
    EXTRACT(MONTH FROM AGE(COALESCE(sm.end_date, CURRENT_DATE), sm.start_date)),
    ' months ',
    EXTRACT(DAY FROM AGE(COALESCE(sm.end_date, CURRENT_DATE), sm.start_date)),
    ' days'
) AS time_mentored
FROM student_mentors sm
JOIN mentors m
    ON sm.mentor_id = m.mentor_id
WHERE sm.student_id = {student_id}
ORDER BY sm.end_date IS NOT NULL, sm.start_date DESC;
""")

student = student_info.iloc[0]

st.title(student["student_name"])

col1, col2 = st.columns([1, 5])

with col1:
    if st.button("← Back"):
        st.switch_page("pages/1_Student_Directory.py")

st.write(f"**Native Language:** {student['native_language']}")
st.write(f"**Date Enrolled:** {student['date_enrolled']}")

attendance = run_query(f"""
SELECT
    COUNT(*) AS total_sessions,
    COUNT(*) FILTER (WHERE attended = true) AS attended_sessions
FROM sessions
WHERE student_id = {student_id};
""")

total_sessions = attendance.iloc[0]["total_sessions"]
attended_sessions = attendance.iloc[0]["attended_sessions"]

attendance_rate = round(
    100 * attended_sessions / total_sessions, 1
) if total_sessions > 0 else 0

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Level", student["english_level"])

with col2:
    st.metric("Attendance", f"{attendance_rate}%")

with col3:
    st.metric("Sessions Completed", f"{attended_sessions} / {total_sessions}")

st.divider()
st.subheader("Mentor History")

if mentor_history.empty:
    st.info("No mentor records found.")
else:
    for index, row in mentor_history.iterrows():
        if pd.isna(row["end_date"]):
            label = "Current Mentor"
        else:
            label = "Previous Mentor"

        with st.container(border=True):
            st.write(f"**{label}:** {row['mentor_name']}")
            st.write(f"**Start Date:** {row['start_date']}")

            if pd.notna(row["end_date"]):
                st.write(f"**End Date:** {row['end_date']}")

            st.write(f"**Time Mentored:** {row['time_mentored']}")
            
assessment_history = run_query(f"""
SELECT
    assessment_level,
    assessment_date,
    attempt_number,
    confidence_fluency_score,
    comprehension_score,
    verb_usage_score,
    pronunciation_score,
    CASE
        WHEN confidence_fluency_score >= 3
         AND comprehension_score >= 3
         AND verb_usage_score >= 3
         AND pronunciation_score >= 3
        THEN 'Ready to Advance'
        ELSE 'Needs More Practice'
    END AS upgrade_status
FROM assessments
WHERE student_id = {student_id}
ORDER BY assessment_date DESC, attempt_number DESC;
""")

st.divider()
st.subheader("Assessment History")

if assessment_history.empty:
    st.info("No assessment recorded yet.")
else:
    for index, row in assessment_history.iterrows():
        with st.container(border=True):
            st.markdown(
                f"**{row['assessment_level']} Assessment**  \n"
                f"Attempt {row['attempt_number']} · {row['assessment_date']}"
            )

            score_map = {
                "Confidence & Fluency": row["confidence_fluency_score"],
                "Comprehension": row["comprehension_score"],
                "Verb Usage": row["verb_usage_score"],
                "Pronunciation": row["pronunciation_score"]
            }

            for label, score in score_map.items():
                st.write(f"**{label}:** {score} / 4")

            if st.button("View Rubric", key=f"rubric_{index}"):
                st.switch_page("pages/6_Assessment_Framework.py")



            