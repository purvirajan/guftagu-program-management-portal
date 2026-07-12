import streamlit as st
from styles import load_css

st.set_page_config(
    page_title="Assessment Framework",
    page_icon="📋",
    layout="wide"
)

load_css()
from auth import require_demo_login, logout_button

col1, col2 = st.columns([1, 6])

with col1:
    if st.button("← Back"):
        st.switch_page("pages/2_Student_Profile.py")

st.title("Assessment Framework")

level = st.radio(
    "Select rubric level",
    ["Beginner", "Intermediate", "Advanced"],
    horizontal=True
)

if level != "Beginner":
    st.info(f"{level} rubric is currently in development.")
    st.stop()

st.markdown("""
<div class="framework-hero">
    <h3>Beginner English Speaking Rubric</h3>
    <p>
        This rubric standardizes beginner-level Guftagu assessments across four speaking competencies.
        Final scores represent the panel's agreed-upon evaluation. This rubric standardizes beginner-level Guftagu assessments across four speaking competencies. Final scores represent the panel's agreed-upon evaluation.
        While this framework provides a consistent method for evaluating progress, I recognize the limitations of quantifying an inherently subjective process such as language acquisition. The rubric is intended to support mentor judgment rather than replace it.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

rubric = {
    "Confidence & Fluency": [
        "Responds with < 3 words",
        "Participates in conversations with 1–5 words, with frequent hesitation",
        "Answers in 1–2 sentences with frequent hesitation",
        "Answers question(s) in 1–2 sentences, no hesitation"
    ],
    "Pronunciation Clarity": [
        "Completely unclear without additional questions",
        "Around half of the statement is understandable",
        "Statement's content can be understood with <5 mispronunciations",
        "Predominantly clear pronunciation"
    ],
    "Verb Usage": [
        "Verb tenses are almost entirely incorrect or not used",
        "Verbs are used correctly but in the wrong tense",
        "Verb usage for 2 tenses are correct",
        "Verb tenses are consistently correct and student can occasionally mix tenses"
    ],
    "Comprehension": [
        "Not able to rephrase the conversation in any language",
        "Able to catch a couple of lines and rephrase them in any language",
        "Able to rephrase most of the ideas in English",
        "Able to accurately rephrase the conversation in English"
    ]
}

st.subheader("Rubric Scale")

for competency, scores in rubric.items():
    with st.container(border=True):
        st.markdown(f"### {competency}")

        cols = st.columns(4)

        for i, description in enumerate(scores):
            with cols[i]:
                st.markdown(f"**{i + 1}**")
                st.write(description)

st.divider()

st.subheader("Assessment Process")

st.markdown("""
1. Mentee completes a beginner-level speaking assessment.
2. Panel reviews the performance using the rubric.
3. Panel agrees on one final score for each competency.
4. Scores are stored in the portal and used to track progress.
""")

st.info(
    "A score of 3 or higher across all four competencies indicates the mentee has met the beginner benchmark."
)