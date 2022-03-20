#!/usr/bin/python3x


"""
SQL setup file, run once

"""


import os
import sqlite3
import config as cfg


query_table_users = """CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER);
        """
query_table_chats = """CREATE TABLE IF NOT EXISTS chats(
            chat_id INTEGER,
            members TEXT);
        """


db = os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), cfg.DB_NAME)
if os.path.isfile(db):
    print("Database already exists, rename or remove and re-run this script.")
else:
    conn = sqlite3.connect(db, check_same_thread=False)
    cur = conn.cursor()
    cur.execute(query_table_users)
    cur.execute(query_table_chats)
    conn.commit()
    conn.close()
    print("Database successfully created.")
