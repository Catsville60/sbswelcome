# -*- coding: utf-8 -*-
"""Welcome bot for new sbs employees"""

import telebot
from telebot import types # для указание типов

#TODO Продумать архитектуру меню
#TODO Функционал примерный (Структура компании, полезные ссылки, материалы касательно плюшек(отпуск, ипотека, больничный, спортзал), полезные контакты, обратная связьб, опросники, )

bot = telebot.TeleBot("6054049215:AAGj-Zr_a0YVc1QxaO8czD-WEh81OMirsKg")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Структура компании")
    btn2 = types.KeyboardButton("Полезные материалы")
    btn3 = types.KeyboardButton("Контакты")
    btn4 = types.KeyboardButton("Обратная связь")
    btn5 = types.KeyboardButton("Обпросники")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Добро пожаловать в Сбербанк-Сервис! Мое предназначение - это облегчить твой 'Онбординг' в компании и поскорее совсем познакомится".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Полезные материалы"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ДМС")
        btn2 = types.KeyboardButton("Отпуск")
        btn3 = types.KeyboardButton("Ипотека")
        btn4 = types.KeyboardButton("Больничный")
        btn5 = types.KeyboardButton("Спорт")
        btn6 = types.KeyboardButton("Полезные ссылки")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, text="Выбери интересующий раздел", reply_markup=markup)

    elif (message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "У меня нет имени..")

    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Поздороваться с читателями")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton(" Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)