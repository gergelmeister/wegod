import sqlite3
import datetime


def new_db():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS users(
           userid INT PRIMARY KEY,
           currency TEXT);
        """)
    conn.commit()


def add_new(user_id):
    conn = sqlite3.connect('users.db')
    user = (int(user_id), "KZT")
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO users(userid, currency) VALUES(?, ?);", user)
    conn.commit()


def change_agreement(user_id, agreement):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute(f"UPDATE users SET agreement = {agreement} WHERE userid = {user_id}")
    conn.commit()


def get_agreement(user_id):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute(f"SELECT agreement FROM users WHERE userid = {user_id}")
    result = cur.fetchall()
    return result[0][0]


def set_last_interaction(user_id):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    time = int(datetime.datetime.utcnow().timestamp())
    cur.execute(f"UPDATE users SET lastinteraction = '{time}' WHERE userid = {user_id}")
    conn.commit()


def get_last_interaction(user_id):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute(f"SELECT lastinteraction FROM users WHERE userid = {user_id}")
    result = cur.fetchall()
    return datetime.datetime(result[0][0])


def get_base():
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    result = cur.fetchall()
    return result


if __name__ == '__main__':
    new_db()