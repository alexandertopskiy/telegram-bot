# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import requests
import json

token = "1185406474:AAG7PO7veHuxp5D_bPjCj_0J5eiaq3gzkUQ"
bot = telebot.TeleBot(token)
bot.delete_webhook()

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('/dog', '/music')
    bot.send_message(message.from_user.id, 
    """Добро пожаловать!
Список доступных команд:
/dog  - Получить случайное фото собаки
/music - Получить список песен группы/исполнителя""", 
    reply_markup=user_markup)


@bot.message_handler(commands=['dog'])
def handle_facts(message):
    result = requests.get("https://bottelegrampy.azurewebsites.net/showDog")
    url = result.text
    bot.send_photo(message.chat.id, url)

@bot.message_handler(commands=['music'])
def time_handler(message):
    msg = bot.send_message(message.chat.id, "Введите название группы/исполнителя\nНапример, Three days Grace")
    bot.register_next_step_handler(msg, get_audios)
    
def get_audios(message):
    try:
        result = requests.get("https://bottelegrampy.azurewebsites.net/showAudio?name={}".format(message.text))
        bot.send_message(message.chat.id, result.text)
    except:
        bot.send_message(message.chat.id, "Не удалось найти данные по этому исполнителю")

bot.polling(none_stop=True, interval=0)

