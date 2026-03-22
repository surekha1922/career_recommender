import psycopg2
from config import get_secret

def get_conn():
    return psycopg2.connect(
        host=get_secret("DB_HOST"),
        database=get_secret("DB_NAME"),
        user=get_secret("DB_USER"),
        password=get_secret("DB_PASS"),
        port=get_secret("DB_PORT"),
        sslmode="require"
    )