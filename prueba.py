import os
import telebot
from telebot import types

API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)

def listener(*mensajes):  ##Cuando llega un mensaje se ejecuta esta función
    for m in mensajes:
        chat_id = m.chat.id
        if m.content_type == 'text':
            text = m.text
            bot.send_message(chat_id,"Me copio de tu texto")
            bot.send_message(chat_id, text)

bot.set_update_listener(listener) #registrar la funcion listener
bot.polling()

while True: #No terminamos nuestro programa
    pass