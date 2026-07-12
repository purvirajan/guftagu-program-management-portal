import streamlit as st
from database import run_query
from styles import load_css

st.set_page_config(
    page_title="Guftagu Progress Portal",
    page_icon="📚",
    layout="wide"
)

load_css()

st.markdown("""
<div class="home-hero">
    <h1>Guftagu Progress Portal</h1>
    <p>
        Supporting spoken English mentorship through assessment,
        attendance tracking, and program management.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="login-card">
    <h2>Explore the Portal</h2>
    <p>Select a role and demo user to view the portal with role-based access.</p>
</div>
""", unsafe_allow_html=True)

center = st.columns([1.3, 1, 1.3])[1]

with center:
    selected_role = st.radio(
        "Choose a workspace",
        ["Student", "Mentor", "Administrator"]
    )

    if selected_role == "Student":
        demo_users = run_query("""
            SELECT
                au.user_id,
                aur.student_id AS profile_id,
                s.student_name AS display_name
            FROM app_users au
            JOIN app_user_roles aur
                ON au.user_id = aur.user_id
            JOIN students s
                ON aur.student_id = s.student_id
            WHERE aur.role = 'student'
            ORDER BY s.student_name;
        """)

    elif selected_role == "Mentor":
        demo_users = run_query("""
            SELECT
                au.user_id,
                aur.mentor_id AS profile_id,
                m.mentor_name AS display_name
            FROM app_users au
            JOIN app_user_roles aur
                ON au.user_id = aur.user_id
            JOIN mentors m
                ON aur.mentor_id = m.mentor_id
            WHERE aur.role = 'mentor'
            ORDER BY m.mentor_name;
        """)

    else:
        demo_users = run_query("""
            SELECT
                au.user_id,
                NULL::INTEGER AS profile_id,
                au.display_name
            FROM app_users au
            JOIN app_user_roles aur
                ON au.user_id = aur.user_id
            WHERE aur.role = 'admin'
            ORDER BY au.display_name;
        """)

    if demo_users.empty:
        st.warning(f"No demo {selected_role.lower()} accounts are available.")
    else:
        selected_name = st.selectbox(
            "Select a demo user",
            demo_users["display_name"]
        )

        selected_user = demo_users.loc[
            demo_users["display_name"] == selected_name
        ].iloc[0]

        if st.button("Continue", use_container_width=True):
            st.session_state["authenticated"] = True
            st.session_state["demo_mode"] = True
            st.session_state["user_id"] = int(selected_user["user_id"])
            st.session_state["selected_role"] = selected_role.lower()

            if selected_role == "Student":
                st.switch_page("pages/2_Student_Profile.py")

            elif selected_role == "Mentor":
                st.session_state["selected_mentor_id"] = int(
                    selected_user["profile_id"]
                )
                st.switch_page("pages/2_Mentor_Dashboard.py")

            else:
                st.switch_page("pages/1_Admin_Dashboard.py")

st.divider()

st.markdown("""
<p class="login-note">
    Portfolio demo using synthetic data. Google authentication will be added later.
</p>
""", unsafe_allow_html=True)