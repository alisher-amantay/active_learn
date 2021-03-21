import time

import torch
from transformers import BertForQuestionAnswering
import telebot

from ipynb.fs.defs.bert import answer_question
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/path/to/application/app/folder')
from telebot import types

bot = telebot.TeleBot('1785934935:AAEQ8wCHxZwCE9ICbn5VLwA_hplfpuguAv0')
bert_abstract=''
question=''

@bot.message_handler(commands=['start','help'])
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
    markup=types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, 'Analyzing...')

    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Change text", callback_data='good')
    item2 = types.InlineKeyboardButton("Enter another question", callback_data='bad')
    markup.add(item1, item2)
    
    bot.send_message(message.chat.id, answer_question(question, bert_abstract))
    doagain(message)

# @bot.callback_query_handler(func=lambda call:True)
# def callback_incline(call):
#     try:
#         if call.message:
#             if call.data == 'yes':
#                 bot.send_message(call.message.chat.id, '')
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="Enter another text",
#                                       reply_markup=None)
#                 bot.register_next_step_handler(call.message, process_text)
#             elif call.data == 'no':
#                 bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                       text="Enter another question",
#                                       reply_markup=None)
#                 bot.register_next_step_handler(call.message, answer)
#
#             # remove inline buttons
#
#     except Exception as e:
#         print(repr(e))

def doagain(message):
    global question
    bot.send_message(message.chat.id, 'Done, try another question)')
    bot.register_next_step_handler(message, answer)

while True:
    try:
        bot.polling(none_stop=True)
    except ():
        time.sleep(5)

