import streamlit as st
from auth import init_auth, logout_user
from otp import send_login_otp, verify_otp

init_auth()

st.set_page_config(page_title="AI SaaS Platform", layout="wide")

# ---------------- LOGOUT HANDLER ----------------
if st.session_state.logged_in:
    with st.sidebar:
        st.success(f"Logged in as: {st.session_state.user}")
        if st.button("Logout"):
            logout_user()
            st.rerun()

# ---------------- LOGIN FLOW ----------------
if not st.session_state.logged_in:

    st.title("🔐 AI SaaS Login")

    email = st.text_input("Enter Email")

    if "otp_sent" not in st.session_state:
        st.session_state.otp_sent = False

    if st.button("Send OTP"):
        if email:
            send_login_otp(email)
            st.session_state.otp_sent = True
            st.success("OTP sent to email")

    if st.session_state.otp_sent:

        otp = st.text_input("Enter OTP")

        if st.button("Verify OTP"):
            if verify_otp(otp):
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid OTP")

# ---------------- MAIN APP AFTER LOGIN ----------------
else:
    st.title("🚀 AI SaaS Dashboard")
    st.info("Use sidebar navigation for features (Home, Dashboard, Roadmap, Help, etc.)")