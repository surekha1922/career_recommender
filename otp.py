import random
import streamlit as st
from email_service import send_otp
from db import get_conn
from auth import login_user

def generate_otp():
    return str(random.randint(100000, 999999))

def send_login_otp(email):

    otp = generate_otp()

    st.session_state["otp"] = otp
    st.session_state["email"] = email

    send_otp(email, otp)

def verify_otp(user_otp):

    if user_otp == st.session_state.get("otp"):

        email = st.session_state["email"]

        conn = get_conn()
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO users(email)
        VALUES (%s)
        ON CONFLICT DO NOTHING
        """, (email,))

        conn.commit()
        conn.close()

        login_user(email)
        return True

    return False