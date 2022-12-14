import sqlite3


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


if __name__ == '__main__':
    new_db()