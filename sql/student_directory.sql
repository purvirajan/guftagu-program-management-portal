SELECT
    st.student_name AS "Student",
    st.english_level AS "Level",
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE se.attended = true) / COUNT(*),
        1
    ) AS "Attendance",
    CASE
        WHEN a.student_id IS NULL THEN 'Not Assessed'
        ELSE 'Assessed'
    END AS "Assessment"
FROM students st
LEFT JOIN sessions se
    ON st.student_id = se.student_id
LEFT JOIN assessments a
    ON st.student_id = a.student_id
GROUP BY
    st.student_name,
    st.english_level,
    a.student_id
ORDER BY st.student_name;