#!/usr/bin/python -u
# -*- coding: utf-8 -*-

import sqlite3 as sql


def recordUser(ID, name, time, chat_id):
    try:
        with sql.connect("nis.db") as con:
            cur = con.cursor()
            query = u"INSERT INTO users (user_id, user_name, last_active, chat_id) VALUES('"
            query += str(ID)
            query += u"', '" + name
            query += u"', '" + time
            query += u"', '" + str(chat_id) + "');"
            cur.execute(query)
            con.commit()
    except Exception as e:
        print(e)
    print("EXE: ", query)


def setAwaitingGrade(ID, Condition):
    try:
        awaiting = ''
        if Condition:
            awaiting = '1'
        else:
            awaiting = '0'
        with sql.connect("nis.db") as con:
            cur = con.cursor()
            query = "UPDATE users SET awaiting_grade = '" + \
                awaiting + "' WHERE user_id = '" + str(ID) + "';"
            cur.execute(query)
            con.commit()
    except Exception as e:
        print(e)
    print("EXE: ", query)


def awaitingGrade(ID):
    try:
        with sql.connect("nis.db") as con:
            cur = con.cursor()
            query = "SELECT awaiting_grade FROM users WHERE user_id = '" + \
                str(ID) + "';"
            cur.execute(query)
            res = cur.fetchone()
            con.commit()
    except Exception as e:
        print(e)
    print("EXE: ", query)
    return res


def schedule(grade, weekday):
    try:
        with sql.connect("nis.db") as con:
            cur = con.cursor()
            query = "SELECT * FROM schedule WHERE grade = '" + \
                str(grade) + "' AND weekday = '" + str(weekday) + "';"
            cur.execute(query)
            res = cur.fetchone()
            con.commit()
    except Exception as e:
        print(e)
    print("EXE: ", query)
    return res


def deleteUser(ID):
    try:
        with sql.connect("nis.db") as con:
            cur = con.cursor()
            query = u"DELETE FROM users WHERE user_id = '" + str(ID) + "';"
            cur.execute(query)
            con.commit()
    except Exception as e:
        print(e)
    print("EXE: ", query)


def user(ID):
    try:
        with sql.connect("nis.db") as con:
            cur = con.cursor()
            query = "SELECT last_active FROM users WHERE user_id = '" + \
                str(ID) + "';"
            cur.execute(query)
            res = cur.fetchall()
            con.commit()
    except Exception as e:
        print(e)
    print("EXE: ", query)
    return res


def recordActivity(ID, time):
    try:
        with sql.connect("nis.db") as con:
            cur = con.cursor()
            query = "UPDATE users SET last_active = '" + \
                time + "' WHERE user_id = '" + str(ID) + "';"
            cur.execute(query)
            con.commit()
    except Exception as e:
        print(e)
    print("EXE: ", query)


def recordMessage(ID, date, time, message):
    try:
        with sql.connect("nis.db") as con:
            cur = con.cursor()
            query = "INSERT INTO messages (from_user, date_sent, time_sent, text_sent) VALUES('"
            query += str(ID)
            query += "', '"
            query += date
            query += "', '"
            query += time
            query += "', '"
            query += message
            query += "');"
            cur.execute(query)
            con.commit()
    except Exception as e:
        print(e)
    print("EXE: ", query)


def activity(ID):
    try:
        with sql.connect("nis.db") as con:
            cur = con.cursor()
            query = "SELECT user_id, last_active FROM users WHERE user_id = '" + \
                str(ID) + "';"
            cur.execute(query)
            res = cur.fetchall()
            con.commit()
    except Exception as e:
        print(e)
    print("EXE: ", query)
    return res


def messages():
    try:
        with sql.connect("nis.db") as con:
            cur = con.cursor()
            query = "SELECT message_id, from_user, text_sent FROM messages"
            cur.execute(query)
            res = cur.fetchall()
            con.commit()
    except Exception as e:
        print(e)
    print("EXE: ", query)
    return res


def username(ID):
    try:
        with sql.connect("nis.db") as con:
            cur = con.cursor()
            query = "SELECT user_name FROM users WHERE users.user_id = '" + \
                str(ID) + "';"
            cur.execute(query)
            res = cur.fetchone()
            con.commit()
    except Exception as e:
        print(e)
    print("EXE: ", query)
    return res


def recordChatID(ID, chat_id):
    try:
        with sql.connect("nis.db") as con:
            cur = con.cursor()
            query = "UPDATE users SET chat_id = '" + \
                str(chat_id) + "' WHERE user_id = '" + str(ID) + "';"
            cur.execute(query)
            con.commit()
    except Exception as e:
        print(e)
    print("EXE: ", query)
