from typing import List

import telebot
# from telebot import types  # для указание типов
import datetime as dt

import os

from dotenv import load_dotenv
from telebot import types

load_dotenv()
token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)


def raschet(count_days_before_sutki: int, frequence_days: int, number_month: int) -> List[int]:
    """
    рассчитываем в какие дни нам на работу

    count_days_before_sutki: оступаем столько дней от сегодня , до того дня когда у нас сутки
    frequence_days: от суток включая их до следующих суток проходит столько дней
    """

    list = []
    if number_month == 1 or number_month == 3 or number_month == 5 or number_month == 7 or number_month == 8 or number_month == 10 or number_month == 12:
        days_in_month = 31
        a = dt.datetime.today().day + count_days_before_sutki # 4
        while (a <= days_in_month):
            list.append(a)
            a += frequence_days # 5
    if number_month == 2:
        days_in_month = 28
        a = dt.datetime.today().day + count_days_before_sutki  # 4
        while (a <= days_in_month):
            list.append(a)
            a += frequence_days
    if number_month == 4 or number_month == 6 or number_month == 9 or number_month == 11:
        days_in_month = 30
        a = dt.datetime.today().day + count_days_before_sutki  # 4
        while (a <= days_in_month):
            list.append(a)
            a += frequence_days
    return list

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ какой график")
    markup.add(btn1, btn2)
    bot.send_message(
        message.chat.id,
        text=f"Привет, {message.from_user.first_name}! Я могу тебе подсказать, когда тебе на работу в этом месяце!",
        reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    current_data = dt.datetime.now()
    current_day = current_data.day
    current_month = current_data.month

    if message.text == "👋 Поздороваться":
        bot.send_message(
            message.chat.id,
            text=(
                f"И снова здравствуйте {message.from_user.first_name}. "
                f"Спасибо что решили сотрудничать!)")
        )
    elif (message.text == "❓ какой график"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1/1")
        btn2 = types.KeyboardButton("1/2")
        btn3 = types.KeyboardButton("1/3")
        btn4 = types.KeyboardButton("1/4")
        btn5 = types.KeyboardButton(
            "никто больше чем 4 дня не отдыхает, не выдумывай!)")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(
            message.chat.id,
            text="1 рабочий/ х - дней отдыха?", reply_markup=markup)

    elif (message.text == "1/1"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton(f"{current_day}")
        btn22 = types.KeyboardButton(f"{current_day + 1}")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn11, btn22, back)
        bot.send_message(
            message.chat.id,
            text="когда тебе на работу?", reply_markup=markup)

    elif (message.text == "1/2"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton(f"{current_day} число")
        btn22 = types.KeyboardButton(f"{current_day + 1} число")
        btn33 = types.KeyboardButton(f"{current_day + 2} число")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn11, btn22, btn33, back)
        bot.send_message(
            message.chat.id,
            text="когда тебе на работу?", reply_markup=markup)

    elif (message.text == "1/3"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton(f"{current_day} ч.")
        btn22 = types.KeyboardButton(f"{current_day + 1} ч.")
        btn33 = types.KeyboardButton(f"{current_day + 2} ч.")
        btn44 = types.KeyboardButton(f"{current_day + 3} ч.")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn11, btn22, btn33, btn44, back)
        bot.send_message(
            message.chat.id,
            text="Какого числа на работу?", reply_markup=markup
        )

    elif (message.text == "1/4"):
        data = dt.datetime.now()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton(f"{current_day} числа")
        btn22 = types.KeyboardButton(f"{current_day + 1} числа")
        btn33 = types.KeyboardButton(f"{current_day + 2} числа")
        btn44 = types.KeyboardButton(f"{current_day + 3} числа")
        btn55 = types.KeyboardButton(f"{current_day + 4} числа")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn11, btn22, btn33, btn44, btn55, back)
        bot.send_message(
            message.chat.id,
            text="Какого числа на работу?", reply_markup=markup
        )

    # ЧИСЛА
    # 4
    elif (message.text == f"{current_day + 4} числа"):
        massiv_job_days = raschet(4, 5, current_month)
        bot.send_message(message.chat.id, text=f"{massiv_job_days}")
    # 3
    elif (message.text == f"{current_day + 3} ч."):
        massiv_job_days = raschet(3, 4, current_month)
        bot.send_message(message.chat.id, text=f"{massiv_job_days}")

    elif (message.text == f"{current_day + 3} числа"):
        massiv_job_days = raschet(3, 5, current_month)
        bot.send_message(message.chat.id, text=f"{massiv_job_days}")


    # 2
    elif (message.text == f"{current_day + 2} число"):
        massiv_job_days = raschet(2, 3, current_month)
        bot.send_message(message.chat.id, text=f"{massiv_job_days}")

    elif (message.text == f"{current_day + 2} ч."):
        massiv_job_days = raschet(2, 4, current_month)
        bot.send_message(message.chat.id, text=f"{massiv_job_days}")

    elif (message.text == f"{current_day + 2} числа"):
        massiv_job_days = raschet(2, 5, current_month)
        bot.send_message(message.chat.id, text=f"{massiv_job_days}")

    # 1
    elif (message.text == f"{current_day + 1}"):
        massiv_job_days = raschet(1, 2, current_month)
        bot.send_message(message.chat.id, text=f"{massiv_job_days}")

    elif (message.text == f"{current_day + 1} число"):
        massiv_job_days = raschet(1, 3, current_month)
        bot.send_message(message.chat.id, text=f"{massiv_job_days}")

    elif (message.text == f"{current_day + 1} ч."):
        massiv_job_days = raschet(1, 4, current_month)
        bot.send_message(message.chat.id, text=f"{massiv_job_days}")

    elif (message.text == f"{current_day + 1} числа"):
        massiv_job_days = raschet(1, 5, current_month)
        bot.send_message(message.chat.id, text=f"{massiv_job_days}")

    # 0
    elif (message.text == f"{current_day}"):
        massiv_job_days = raschet(0, 2, current_month)
        bot.send_message(message.chat.id, text=f"{massiv_job_days}")

    elif (message.text == f"{current_day} число"):
        massiv_job_days = raschet(0, 3, current_month)
        bot.send_message(message.chat.id, text=f"{massiv_job_days}")

    elif (message.text == f"{current_day} ч."):
        massiv_job_days = raschet(0, 4, current_month)
        bot.send_message(message.chat.id, text=f"{massiv_job_days}")

    elif message.text == f"{current_day} числа":
        massiv_job_days = raschet(0, 5, current_month)
        bot.send_message(message.chat.id, text=f"{massiv_job_days}")

    elif message.text == "Вернуться в главное меню" or "вернуться":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ какой график")
        markup.add(button1, button2)
        bot.send_message(
            message.chat.id,
            text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(
            message.chat.id,
            text="На такую комманду я не запрограммирован"
        )


bot.polling(none_stop=True)
