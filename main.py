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
    btn2 = types.KeyboardButton("Расписание БО231ЗСС")
    markup.add(btn1, btn2)
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


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Расписание БО231ЗСС"):
        url = "https://dvgups.ru/index.php?itemid=1246&option=com_timetable&view=newtimetable"
        payload = [('GroupID', "52215")]
        resp = requests.post(url, data=payload)
        soup = bs4.BeautifulSoup(resp.text, 'lxml')
        block = soup.find_all("table", class_="table table-hover table-bordered")
        date_in = 10
        for item in block:
            data_day = item.find_all("tr", class_="d-flex")
            if date_in == 15:
                date_in = date_in + 3
            else:
                date_in = date_in + 1
            print(date_in)
            bot.send_message(message.chat.id, date_in)
            for item in data_day:
                bot.send_message(message.chat.id, item.text.strip())

# @bot.message_handler(commands=['start']) #создаем команду
# def start(message):
#     markup = types.InlineKeyboardMarkup()
#     button1 = types.InlineKeyboardButton("Сайт создателей бота", url='https://habr.com/ru/all/')
#     markup.add(button1)
#     bot.send_message(message.chat.id, "Салам алейкум, напиши /help, чтобы узнать что я умею".format(message.from_user), reply_markup=markup)


# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, text="Салам алейкум, напиши /help, чтобы узнать что я умею")

@bot.message_handler(commands=['help'])
def func(message):
    if (message.text == "Помощь"):
        bot.send_message(message.chat.id, 'Я могу выполнить эти команды: /anekdot, /poem, /bible, /coin, /usd')

@bot.message_handler(commands=['anekdot'])
def search(message):
    url = 'https://www.anekdot.ru/random/anekdot/'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    anek = bs.find('div', class_="text")
    bot.send_message(message.chat.id, anek.text)

@bot.message_handler(commands=['poem'])
def search_poem(message):
    url = 'https://millionstatusov.ru/random.html?category_id=3'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    poema = bs.find('div', class_="cont_text")
    bot.send_message(message.chat.id, poema.text)

@bot.message_handler(commands=['usd'])
def search_usd(message):
    url = 'https://quote.rbc.ru/ticker/59111'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    ric = bs.find_all('div', class_="chart__info__row js-ticker")
    for rih in ric:
        header = rih.find('span', class_='chart__info__sum')
        bot.send_message(message.chat.id, header.text)


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







@bot.message_handler(commands=['bible'])
def search_bible(message):
    url = 'https://dailyverses.net/ru/%D1%81%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D1%8B%D0%B9-%D1%81%D1%82%D0%B8%D1%85-%D0%B8%D0%B7-%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%B8'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    bibl = bs.find_all('div', class_="b1")
    for channel in bibl:
        header = channel.find('span', class_='v1')
        named = channel.find('a', class_='vc')
        bot.send_message(message.chat.id, header.text)
        bot.send_message(message.chat.id, named.text)

@bot.message_handler(commands=['coin'])
def coin(message):
    choice = random.randint(1, 2)
    if choice == 1:
        result = "Орёл"
    elif choice == 2:
        result = "Решка"
    bot.send_message(message.chat.id, result)


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, 'Тормози родной, напиши /help, чтобы узнать список доступных команд.')


bot.polling()
