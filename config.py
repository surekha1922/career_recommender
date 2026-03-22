import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # works only locally

def get_secret(key):
    """
    Priority:
    1. Streamlit Cloud secrets
    2. Local .env file
    """

    try:
        return st.secrets[key]
    except Exception:
        return os.getenv(key)