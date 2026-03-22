from db import conn

def get_users():
    c = conn()
    cur = c.cursor()
    cur.execute("SELECT username,email,role FROM users")
    return cur.fetchall()


def get_history():
    c = conn()
    cur = c.cursor()
    cur.execute("SELECT * FROM history")
    return cur.fetchall()