#!/usr/bin/python3x


"""
SQL functions file

"""


import os
import sqlite3
import config as cfg


# Initialization
db = os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), cfg.DB_NAME)
conn = sqlite3.connect(db, check_same_thread=False)
cur = conn.cursor()


# Users
# Check if user registered
def check_if_user_exists(user_id):
    cur.execute("SELECT user_id FROM users WHERE user_id = '{}'".format(user_id))
    result = cur.fetchall()
    if len(result) > 0:
        return True
    else:
        return False


# Register new user
def save_user(user_id):
    query = "INSERT INTO users VALUES (?)"
    cur.execute(query, (user_id,))
    conn.commit()


# Chats
# Save members for chat
def save_chat_members(chat_id, members_list):
    cur.execute("SELECT chat_id FROM chats WHERE chat_id = '{}'".format(chat_id))
    result = cur.fetchall()
    if len(result) > 0:
        cur.execute("UPDATE chats SET members = '{}' WHERE chat_id = '{}'".format(members_list, chat_id))
        conn.commit()
    else:
        query = "INSERT INTO chats VALUES (?, ?)"
        cur.execute(query, (chat_id, members_list,))
        conn.commit()


# Get members for chat
def get_chat_members(chat_id):
    cur.execute("SELECT members FROM chats WHERE chat_id = '{}'".format(chat_id))
    result = cur.fetchall()
    return result


# Util
# Close database connection
def close():
    conn.close()
    print("Соединение с базой данных закрыто.")
