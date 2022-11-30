import time
import sys
sys.path.insert(1, '/path/to/application/app/folder')

import torch
from transformers import BertForQuestionAnswering
import telebot
from telebot import types

from utils.inference import answer_question


TELEBOT_TOKEN = ''  # input token here
bot = telebot.TeleBot(TELEBOT_TOKEN)
bert_abstract = ''
question = ''


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hello! Enter your text')
    bot.register_next_step_handler(message, process_text)


def process_text(message):
    global bert_abstract
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, 'Enter your question')
    bert_abstract = message.text
    bot.register_next_step_handler(message, answer)


def answer(message):
    global question
    question = message.text
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, 'Analyzing...')

    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Change text", callback_data='good')
    item2 = types.InlineKeyboardButton("Enter another question", callback_data='bad')
    markup.add(item1, item2)

    bot.send_message(message.chat.id, answer_question(question, bert_abstract))
    do_again(message)


def do_again(message):
    global question
    bot.send_message(message.chat.id, 'Done, try another question)')
    bot.register_next_step_handler(message, answer)


while True:
    try:
        bot.polling(none_stop=True)
    except:
        time.sleep(5)
