#! /usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import requests

token = "1185406474:AAG7PO7veHuxp5D_bPjCj_0J5eiaq3gzkUQ"
bot = telebot.TeleBot(token)
bot.delete_webhook()

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('/weather', '/time')
    bot.send_message(message.from_user.id, 
    """Добро пожаловать!
Список доступных команд:
/weather - Узнать прогноз погоды на ближайшие дни
/time - Узнать текущее время в 5 столицах мира""", 
    reply_markup=user_markup)

@bot.message_handler(commands=['weather'])
def handle_check(message):
    msg = bot.send_message(message.chat.id, "Введите город на английском(например, Moscow): ")
    bot.register_next_step_handler(msg, weather_step)

def weather_step(message):
    city = message.text + ",ru"
    try:
        uri = "https://bottelegrampy.azurewebsites.net/weather?city={}".format(city)
        result = requests.get(uri)
        bot.send_message(message.chat.id, result.text)
    except:
        bot.send_message(message.chat.id, "Возникла ошибка. Попробуйте снова...")

@bot.message_handler(commands=['time'])
def time_handler(message):
    result = requests.get("https://bottelegrampy.azurewebsites.net/TimeFunc")
    bot.send_message(message.chat.id, result.text)

bot.polling(none_stop=True, interval=0)