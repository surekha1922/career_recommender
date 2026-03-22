import streamlit as st
from db import get_conn

st.title("📜 History")

conn = get_conn()
cur = conn.cursor()

cur.execute("SELECT * FROM analysis")
rows = cur.fetchall()

for r in rows:
    st.write(r)