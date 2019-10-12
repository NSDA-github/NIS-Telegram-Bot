#!/usr/bin/python -u
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup

token = ""


def welcome(bot, update, kb_markup):
    response = u'Привет, ' + update.message.from_user.first_name + \
        u'. Я бот от НИШ Уральск и в будущем я должен стать вашим ассистентом по школьным вопросам.'
    bot.send_message(chat_id=update.message.chat_id, text=response)
    bot.send_message(chat_id=update.message.chat_id,
                     text='Сейчас я могу только показывать расписания и принимать ваши сообщения в ящик предложений.')
    bot.send_message(chat_id=update.message.chat_id,
                     text='Для помощи, введите /help.', reply_markup=kb_markup)


def help(bot, update, kb_markup):
    response = u'Добрый день. Я бот от НИШ Уральск.'
    bot.send_message(chat_id=update.message.chat_id, text=response)
    response = u'Если мой собеседник присылает мне команду /shedule, я, получив ответ, отправляю расписание запрошенного класса.'
    bot.send_message(chat_id=update.message.chat_id, text=response)
    response = u'В остальных случаях я принимаю ваши сообщения прямо в ящик предложений!'
    bot.send_message(chat_id=update.message.chat_id,
                     text=response, reply_markup=kb_markup)


def register(bot, update, kb_markup):
    bot.send_message(chat_id=update.message.chat_id,
                     text='Я не могу вам ответить :(. Зарегистрируйтесь в моей системе, просто введите /start.', reply_markup=kb_markup)


def schedule(bot, update, kb_markup, res):
    for subject in res:
        bot.send_message(chat_id=update.message.chat_id,
                         text=subject, reply_markup=kb_markup)


def sendGrade(bot, update, kb_markup):
    bot.send_message(chat_id=update.message.chat_id,
                     text='Пожалуйста, отправьте какой класс хотите посмотреть в формате "7A", "10C" [КлассБуква].', reply_markup=kb_markup)


def wrongGrade(bot, update, kb_markup):
    bot.send_message(chat_id=update.message.chat_id,
                     text='Вы ввели не правильный класс, продолжаю принимать сообщения в ящик предложений.', reply_markup=kb_markup)


def wait(bot, update, kb_markup):
    bot.send_message(chat_id=update.message.chat_id,
                     text='Я могу не успеть все обработать. Пожалуйста, подождите минуту перед отправлением нового сообщения. Спасибо!', reply_markup=kb_markup)


def received(bot, update, kb_markup, text):
    response = update.message.from_user.first_name + \
        u', я получил Ваше сообщение: "' + text + \
        u'". Спасибо!'
    bot.send_message(chat_id=update.message.chat_id, text=response)
    bot.send_message(chat_id=update.message.chat_id,
                     text='Все сообщения сохраняются в ящик предложений и будут видны Student Council.', reply_markup=kb_markup)
