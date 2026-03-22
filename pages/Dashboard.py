import streamlit as st
from ml_engine import calculate_score
from db import get_conn
from report import generate_pdf
import uuid

st.title("📊 Dashboard")

job = st.text_area("Job Description")
resume = st.text_area("Resume")

if st.button("Analyze"):

    score, matched, missing = calculate_score(resume, job)

    st.metric("Score", f"{score}%")
    st.write("Matched:", matched)
    st.write("Missing:", missing)

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO analysis(email, role, score, matched, missing)
    VALUES (%s,%s,%s,%s,%s)
    """, (st.session_state.get("user","guest"), "ML", score, str(matched), str(missing)))

    conn.commit()
    conn.close()

    file = f"report_{uuid.uuid4().hex[:6]}.pdf"
    generate_pdf(file, "user", score, "ML", matched, missing)

    with open(file, "rb") as f:
        st.download_button(
            "📄 Download Report",
            f.read(),
            file_name="resume_report.pdf",
            mime="application/pdf"
        )