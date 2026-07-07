import streamlit as st
from database import run_query

st.set_page_config(
    page_title="Student Profile",
    page_icon="👤",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1 {
    color: #2C5282;
    font-size: 2.5rem;
    font-weight: 700;
}

[data-testid="stMetric"] {
    background: linear-gradient(135deg, #E8F1FD, #FFFFFF);
    border-left: 6px solid #4285F4;
    padding: 1rem;
    border-radius: 14px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.08);
}

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

if "selected_student_id" not in st.session_state:
    st.warning("Please select a student from the Student Directory.")
    st.stop()

student_id = st.session_state["selected_student_id"]

student_info = run_query(f"""
SELECT
    student_name,
    native_language,
    english_level,
    date_enrolled
FROM students
WHERE student_id = {student_id};
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
    st.dataframe(
        assessment_history,
        use_container_width=True,
        hide_index=True
    )