import os
import telebot
from telebot import types

API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, 'Hey! hows it going?')

@bot.message_handler(commands=['Hello'])
def hello(message):
    bot.send_message(message.chat.id, 'Hello!')



@bot.message_handler(commands=['cal'])
def welcome(message):
   # print(message)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Trapezoid', 'Simpson')
    reply = bot.reply_to(message, "Select computation method" ,reply_markup=markup)
    bot.register_next_step_handler(reply, markup_handler)

def markup_handler(message):
    if(message.text == 'Trapezoid'):
        bot.send_message(message.chat.id, "Trapezoid Block")
    elif(message.text == 'Simpson'):
        bot.send_message(message.chat.id, "Simpson Block")

bot.polling()

*****************************
import os
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
                               InlineKeyboardButton("No", callback_data="cb_no"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "Answer is Yes")
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Answer is No")

@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())

bot.infinity_polling()










@bot.message_handler(content_types=["text"], func=lambda message: message.text == "Prueba")
def func2(message):
    keyboard = types.InlineKeyboardMarkup()
    url_btn = types.InlineKeyboardButton(url="https://stackoverflow.com", text="Informacion de Prueba")
    keyboard.add(url_btn)
    bot.send_message(message.chat.id, "aqui esta la informacion de Prueba", reply_markup=keyboard)