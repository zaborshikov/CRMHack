import sqlite3
import creds
from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import get_wordcloud

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['CORD_HEADERS'] = 'Content-Type'
conn = sqlite3.connect('moods.db')
cur = conn.cursor()

@app.route("/foto", methods=['POST'])
def foto():
    id = int(request.get_json()['id'])
    sqlite_select_query = """SELECT * from moods where moodsid = ?"""
    cur.execute(sqlite_select_query, (id, ))
    res = cur.fetchall()
    tex = ''
    for i in res:
        tex += str(i[3]) + " "
    get_wordcloud.get_word_cloud(tex)
    lin = ''
    with open('words.png') as f:
        lines = f.readlines
        for i in lines:
            lin += i + '\n'
    return lin


@app.route("/stats", methods=['POST'])
def stats():
    id = int(request.get_json()['id'])
    sqlite_select_query = """SELECT * from moods where moodsid = ?"""
    cur.execute(sqlite_select_query, (id, ))
    res = cur.fetchall()
    pos = neg = net = ''
    for i in res:
        if 'None' not in i[1]:
            pos += str(i[1]) + ' '
        elif 'None' not in i[2]:
            neg += str(i[2]) + ' '
        else:
            net += str(i[4]) + ' '
    return 'POSITIVE: ' + pos + 'NEGATIVE: ' + neg + 'NEUTRAL: ' + net



@app.route("/get_brands", methods=['GET'])
def get_brands():
    conn = sqlite3.connect('moods.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM moods")
    res = cur.fetchall()
    lol = ''
    for i in res:
        if str(-i[0]) not in lol:
            lol += Database.create2(-i[0]) + ' ' + str(-i[0]) + " "
    return lol


@app.route("/create", methods=['POST'])
def create():
    shortname = request.get_json()['vk_link']
    result = creds.vk.groups.getById(group_ids=shortname, group_id=shortname)
    id_company = str(result[0]['id'])
    return str(id_company)


@app.route("/comment_analyse", methods=['GET'])
def comment_analyse(id):
    id = request.get_json()['id']
    if request.method == 'GET':
        try:
            sqlite_connection = sqlite3.connect('moods.db')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")

            sqlite_select_query = """SELECT * from moods where moodsid = ?"""
            cursor.execute(sqlite_select_query, (id, ))
            print("Чтение одной строки \n")
            records = cursor.fetchmany(all)
            plu = minu = poh = ""
            for i in records:
                if 'None' not in i[1]:
                    plu += str(i[3]) + ' '
                elif 'None' not in i[2]:
                    minu += str(i[3]) + ' '
                else:
                    poh += str(i[3]) + ' '
            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")
            return '[' + plu + '], [' + minu + '], [' + poh + ']'
    else:
        pass


class Database:
    def create(shortname):
        result = creds.vk.groups.getById(group_ids=shortname, group_id=shortname)
        id_company = str(result[0]['id'])
        return("-" + id_company)
    def create2(shortname):
        result = creds.vk.groups.getById(group_ids=shortname, group_id=shortname)
        name_company = str(result[0]['name'])
        return(name_company)
    def setPos(id, positive, message):
        print(message)
        cur.execute(f"insert into moods (positive, moodsid, comment) values ({positive}, {id}, '{message}')")
        conn.commit()

    def setNeg(id, negative, message):
        cur.execute(f"insert into moods (negative, moodsid, comment) values ({negative}, {id}, '{message}')")
        conn.commit()
    def setNeutral(id, neutral, message):
        cur.execute(f"insert into moods (neutral, moodsid, comment) values ({neutral}, {id}, '{message}')")
        conn.commit()

    def getIDs():
        cur.execute("SELECT * FROM companyid")
        res = cur.fetchone()
        return(res)

    def getMood():
        cur.execute("SELECT * FROM moods")
        res = cur.fetchone()
        return res
    def comment_analyse(id):
        try:
            sqlite_connection = sqlite3.connect('moods.db')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")

            sqlite_select_query = """SELECT * from moods where moodsid = ?"""
            cursor.execute(sqlite_select_query, (id, ))
            print("Чтение одной строки \n")
            records = cursor.fetchmany()
            plu = minu = poh = []
            for i in records:
                if 'None' not in i[1]:
                    plu.append(i[3])
                elif 'None' not in i[2]:
                    minu.append(i[3])
                else:
                    poh.append(i[3])
            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")
            return plu, minu, poh
    def get_brands():
        cur.execute("""SELECT * from moods""")
        res = cur.fetchall()
        lol = []
        for i in res:
            if -i[0] not in lol:
                lol.append(-i[0])
        return lol

# print(Database.get_brands())
app.run(debug=True)