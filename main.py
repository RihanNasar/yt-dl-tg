from yt_dlp import YoutubeDL
from dotenv import load_dotenv
import os
import telebot
from telebot import types
import re

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


def is_youtube_url(link):
    youtube_url_pattern = r'https?://(?:www\.)?youtube\.com/watch\?v=[\w-]+|https?://youtu\.be/[\w-]+'
    return bool(re.match(youtube_url_pattern, link))


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f"Enter the link of the video {message.text}")


@bot.message_handler()
def handle_start_help(message):
    if (is_youtube_url(message.text)):
        markup = types.ReplyKeyboardMarkup()
        itembtna = types.KeyboardButton('audio')
        itembtnv = types.KeyboardButton('best quality')
        itembtnc = types.KeyboardButton('720p')
        itembtnd = types.KeyboardButton('480p')
        itembtne = types.KeyboardButton('360p')
        markup.row(itembtna, itembtnv)
        markup.row(itembtnc, itembtnd, itembtne)
        bot.send_message(message.chat.id, "Choose your preferred format:",
                         reply_markup=markup)
    else:
        bot.reply_to(message, "not a youtube link")
# URLS = input("Enter the url : ")
# with YoutubeDL() as ydl:
#     ydl.download(URLS)


bot.infinity_polling()
