from telebot import TeleBot
from telebot.types import Message

bot = TeleBot("7904721231:AAGq1OOZt4wOgBTwIZZJYzL4xLl6DgspAsk")

@bot.message_handler(commands=['start', 'info'])
def handle_start_info(message: Message):
    chat_id = message.chat.id
    if message.text == 'start':
        bot.send_message(chat_id, f"Salom Sportchilar haqida malumot ")
    elif message.text == 'info':
        bot.send_message(chat_id, "Boks, Kurash ")

@bot.message_handler(commands=['help'])
def handle_help(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Bizning kompaniya haqida malumot.")

@bot.message_handler(content_types=['text'])
def handle_text(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Siz yozdingiz: {message.text}")
bot.polling()
