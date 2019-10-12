#!/usr/bin/python -u
# -*- coding: utf-8 -*-

import random
import datetime
import sys
from libs import respond
from libs import sql_query as sql
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup

token = str(sys.argv[1])
respond.token = token

updater = Updater(token=token)
dispatcher = updater.dispatcher

kb_def = [[KeyboardButton('/help')], [KeyboardButton('/schedule')]]
kb_reg = [[KeyboardButton('/start')]]
kb_markup = ReplyKeyboardMarkup(kb_def, resize_keyboard=True)
kb_markup_reg = ReplyKeyboardMarkup(kb_reg, resize_keyboard=True)


def startCommand(bot, update):
    try:
        respond.welcome(bot, update, kb_markup)

        if not update.message.from_user.is_bot:
            res = sql.user(update.message.from_user.id)
            if len(res) == 0:
                sql.recordUser(update.message.from_user.id,
                               update.message.from_user.first_name,
                               datetime.datetime.now().strftime("%H:%M:%S"),
                               update.message.chat_id)
            else:
                sql.deleteUser(update.message.from_user.id)
                sql.recordUser(update.message.from_user.id,
                               update.message.from_user.first_name,
                               datetime.datetime.now().strftime("%H:%M:%S"),
                               update.message.chat_id)
    except Exception as e:
        print(e)


def textMessage(bot, update):
    try:
        allow = False
        res = sql.user(update.message.from_user.id)
        if len(res) == 0:
            respond.register(bot, update, kb_markup_reg)
        else:
            sql.recordActivity(update.message.from_user.id,
                               datetime.datetime.now().strftime("%H:%M:%S"))
            sql.recordChatID(update.message.from_user.id,
                             update.message.chat_id)
            allow = True

        if allow:
            res = sql.awaitingGrade(update.message.from_user.id)
            if not res[0]:
                respond.received(bot, update, kb_markup, update.message.text)
                sql.recordMessage(update.message.from_user.id,
                                  datetime.datetime.now().strftime("%Y-%m-%d"),
                                  datetime.datetime.now().strftime("%H:%M:%S"),
                                  update.message.text)
            else:
                sql.setAwaitingGrade(update.message.from_user.id, False)
                res = sql.schedule(
                    # update.message.text, datetime.datetime.today().weekday())
                    update.message.text, 0)
                if(res):
                    respond.schedule(bot, update, kb_markup, res[2:])
                else:
                    respond.wrongGrade(bot, update, kb_markup)
    except Exception as e:
        print(e)


def individualreq(bot, update, args):
    try:
        id = update.message.text

        id = id[1:]
        if id == 'help':
            respond.help(bot, update, kb_markup)
            sql.recordChatID(update.message.from_user.id,
                             update.message.chat_id)
        if id == 'schedule':
            sql.setAwaitingGrade(update.message.from_user.id, True)
            respond.sendGrade(bot, update, kb_markup)
    except Exception as e:
        print(e)


start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(CommandHandler(
    ['help', 'schedule'], individualreq, pass_args=True))

updater.start_polling(clean=True)

updater.idle()
