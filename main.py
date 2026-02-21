import os
import telebot
from telebot import types
from dotenv import load_dotenv
from logic import translate_to_hacker

load_dotenv()
MY_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(MY_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Напиши слово или фразу и я переведу его в хакерский язык")


@bot.message_handler(func=lambda message: True)
def handle_message(message: types.Message):

    user_text = message.text
    hacker_result = translate_to_hacker(user_text)


    bot.reply_to(message, hacker_result)


bot.polling()