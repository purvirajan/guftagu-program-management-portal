import streamlit as st
from database import run_query


def require_login():
    if not st.session_state.get("authenticated", False):
        st.warning("Please log in from the homepage.")
        st.stop()


def logout_button():
    if st.button("Log out"):
        st.session_state.clear()
        st.switch_page("Overview.py")


def get_current_user_id():
    user_id = st.session_state.get("user_id")

    if user_id is None:
        st.error("No logged-in user was found.")
        st.stop()

    return int(user_id)


def get_selected_role():
    selected_role = st.session_state.get("selected_role")

    if selected_role is None:
        st.error("No workspace role was selected.")
        st.stop()

    return selected_role


def get_current_student_id():
    user_id = get_current_user_id()

    result = run_query(f"""
    SELECT student_id
    FROM app_user_roles
    WHERE user_id = {user_id}
      AND role = 'student';
    """)

    if result.empty or result.iloc[0]["student_id"] is None:
        st.error("This account is not linked to a mentee profile.")
        st.stop()

    return int(result.iloc[0]["student_id"])


def get_current_mentor_id():
    user_id = get_current_user_id()

    result = run_query(f"""
    SELECT mentor_id
    FROM app_user_roles
    WHERE user_id = {user_id}
      AND role = 'mentor';
    """)

    if result.empty or result.iloc[0]["mentor_id"] is None:
        st.error("This account is not linked to a mentor profile.")
        st.stop()

    return int(result.iloc[0]["mentor_id"])