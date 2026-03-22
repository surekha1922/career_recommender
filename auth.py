import streamlit as st

def init_auth():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "user" not in st.session_state:
        st.session_state.user = None

def login_user(email):
    st.session_state.logged_in = True
    st.session_state.user = email

def logout_user():
    st.session_state.logged_in = False
    st.session_state.user = None