#!/usr/bin/python3x

"""
Main file

"""


import telebot
from time import sleep
from signal import signal, SIGINT
import utilities as utils
import sqlighter as db
import config as cfg


# Initialization
bot = telebot.TeleBot(cfg.TOKEN)


# Commands
@bot.message_handler(commands=['start'])
def start(message):
    if utils.check_user_is_registered(message):
        bot.send_message(message.chat.id, cfg.TEXT_GREETINGS_AGAIN)
    else:
        bot.send_message(message.chat.id, cfg.TEXT_GREETINGS)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, cfg.TEXT_HELP)


# Text messages
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_messages(message):
    message_text = message.text
    if message.chat.type == "private":
        bot.send_message(message.chat.id, cfg.ERR_WRONG_USAGE)
    elif message.chat.type == "group" or message.chat.type == "supergroup":  # Somewhy some private groups show as super-
        if message_text.startswith("/add"):
            if utils.save_chat_members(message):
                bot.reply_to(message, cfg.MEMBERS_SAVED)
            else:
                bot.reply_to(message, cfg.MEMBERS_UPDATED)
        elif "@all" in message.text:
            mention = utils.get_chat_members(message)
            bot.reply_to(message, mention)
        elif "Слава Украине" in message.text or "Слава Україні!" in message.text:
            bot.reply_to(message, "Героям слава")
    elif message.chat.type == "channel":
        bot.send_message(message.chat.id, cfg.ERR_GROUPS_ONLY)


# /test
@bot.message_handler(commands=['test'])
def test(message):
    bot.send_photo(message.chat.id, photo="https://funart.pro/uploads/posts/2021-07/1627460721_6-funart-pro-p-koti-palets-vverkh-zhivotnie-krasivo-foto-6.jpg", caption='Я в порядке')


# Other messages
@bot.message_handler(func=lambda message: True, content_types=['sticker'])
def msg_not_recognized_sticker(message):
    bot.send_sticker(message.chat.id, "CAACAgQAAxkBAAEEN6xiNyhEU0K0JoyWstwR_zG4KplSowACOgADzMbLEXdDcDaH7QVAIwQ")
    # Make it reply only when mentioned


@bot.message_handler(func=lambda message: True, content_types=['photo', 'video', 'audio', 'voice', 'video_note', 'text', 'document', 'contact', 'location'])
def msg_not_recognized_photo(message):
    bot.send_message(message.chat.id, cfg.ERR_USE_COMMANDS)


# Util
def cleanup_and_exit(sigint, frame):  # Args show unused, replace with something more neat
    db.close()
    print("Бот остановлен.")
    exit(0)


# Main
def main():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            sleep(1)


# On run
if __name__ == "__main__":
    signal(SIGINT, cleanup_and_exit)
    print("Бот запущен, для выхода - Ctrl+C")
    main()
