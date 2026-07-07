WITH attendance_summary AS (
    SELECT
        student_id,
        COUNT(*) AS total_sessions,
        COUNT(*) FILTER (WHERE attended = true) AS attended_sessions
    FROM sessions
    GROUP BY student_id
),

latest_assessment AS (
    SELECT DISTINCT ON (student_id)
        student_id,
        assessment_date
    FROM assessments
    ORDER BY student_id, assessment_date DESC
)

SELECT
    st.student_id,
    st.student_name AS "Student",
    st.english_level AS "Level",
    ROUND(
        100.0 * COALESCE(att.attended_sessions, 0) / NULLIF(att.total_sessions, 0),
        1
    ) AS "Attendance",
    CASE
        WHEN la.assessment_date IS NULL THEN 'Not Assessed'
        ELSE TO_CHAR(la.assessment_date, 'Mon DD, YYYY')
    END AS "Last Assessment"
FROM students st
LEFT JOIN attendance_summary att
    ON st.student_id = att.student_id
LEFT JOIN latest_assessment la
    ON st.student_id = la.student_id
ORDER BY st.student_name;