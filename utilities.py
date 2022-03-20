#!/usr/bin/python3x


"""
Telebot functions file

"""


import sqlighter as db


# Users
# Check if user registered or is admin
def check_user_is_registered(message):
    if not db.check_if_user_exists(message.from_user.id):
        save_user(message)
        return False
    else:
        return True


# Save new user to db
def save_user(message):
    user_id = message.from_user.id
    db.save_user(user_id)


def save_chat_members(message):
    chat_id = message.chat.id
    members = message.text
    members = members.replace("/add ", "")
    db.save_chat_members(chat_id, members)


def get_chat_members(message):
    members = db.get_chat_members(message.chat.id)
    # You can always look at three things - how the fire burns, how the water flows and how Sqlite3 returns tuple of tuples for every hecking sneeze!
    members, = members  # tuples -> tuple
    members, = members  # tuple -> string
    return members
