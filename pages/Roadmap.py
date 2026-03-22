import streamlit as st
from roadmap_engine import advanced_suggest

st.title("🧭 AI Career Roadmap Analyzer")

# ---------------- BASIC SKILLS ----------------
st.subheader("📌 Core Skills Selection")

skills = [
    "python", "java", "c++", "javascript",
    "machine learning", "deep learning",
    "sql", "docker", "aws",
    "html", "css", "react",
    "cybersecurity", "linux"
]

selected_skills = []

cols = st.columns(3)
for i, skill in enumerate(skills):
    if cols[i % 3].checkbox(skill):
        selected_skills.append(skill)

# ---------------- PROFICIENCY INPUT ----------------
st.subheader("💡 Skill Proficiency Levels")

coding_level = st.slider("Coding Strength (1 - Beginner, 10 - Expert)", 1, 10, 5)
dsa_level = st.slider("DSA Level (1 - Weak, 10 - Strong)", 1, 10, 5)

st.subheader("🗣 Language Proficiency")

english = st.slider("English Communication", 1, 10, 5)
communication = st.slider("General Communication Skills", 1, 10, 5)

# ---------------- ANALYZE BUTTON ----------------
if st.button("Generate Career Roadmap"):

    from roadmap_engine import advanced_suggest

    result = advanced_suggest(
        selected_skills,
        coding_level,
        dsa_level,
        english,
        communication
    )

    st.success("🎯 Career Analysis Completed")

    st.subheader("🏆 Best Career Match")
    st.write(result["best_role"])

    st.subheader("📊 Detailed Scores")

    for role, data in result["all_roles"].items():
        st.write(f"### {role}")
        st.write(f"Skill Match Score: {data['skill_score']}%")
        st.write(f"Coding Fit: {data['coding_fit']}")
        st.write(f"DSA Fit: {data['dsa_fit']}")
        st.write(f"Communication Fit: {data['communication_fit']}")
        st.write("---")

    st.subheader("🧠 Explanation")
    st.info(result["explanation"])