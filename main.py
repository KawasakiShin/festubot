import telebot
from bs4 import BeautifulSoup
import requests
import lxml
from telebot import types
import random
import json
import random
import re
import os
import bs4

bot = telebot.TeleBot('6096647439:AAHInzW860SStinlCOY0HwDGBFUDYLMYCnM')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Расписание БО931ПМИ")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Салам алейкум".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Расписание БО931ПМИ"):
        url = "https://dvgups.ru/index.php?itemid=1246&option=com_timetable&view=newtimetable"
        payload = [('GroupID', "52133")]
        resp = requests.post(url, data=payload)
        soup = bs4.BeautifulSoup(resp.text, 'lxml')
        block = soup.find_all("table", class_="table table-hover table-bordered")
        date_in = 10
        for item in block:
            data_day = item.find_all("tr", class_="d-flex")
            if date_in == 16:
                date_in = date_in + 2
            else:
                date_in = date_in + 1
            print(date_in)
            bot.send_message(message.chat.id, date_in)
            for item in data_day:
                bot.send_message(message.chat.id, item.text.strip())

@bot.message_handler(commands=['festu'])
def search_festu(message):
    url = "https://dvgups.ru/index.php?itemid=1246&option=com_timetable&view=newtimetable"
    payload = [('GroupID', "52215")]
    resp = requests.post(url, data=payload)
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    block = soup.find_all("table", class_="table table-hover table-bordered")
    for item in block:
        data_day = item.find_all("tr", class_="d-flex")
        timetable_data = []
        date_dat = soup.find("h3").text
        for item in data_day:
            bot.send_message(message.chat.id, item.text.strip())

bot.polling()
