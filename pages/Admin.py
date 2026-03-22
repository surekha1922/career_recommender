import streamlit as st
from db import get_conn

st.title("🔐 Admin Panel")

conn = get_conn()
cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM users")
users = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM analysis")
analysis = cur.fetchone()[0]

st.metric("Total Users", users)
st.metric("Total Analyses", analysis)