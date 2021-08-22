import sqlite3

from werkzeug.datastructures import Accept
import creds
from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import get_wordcloud

white = ['http://74bf-85-30-217-217.ngrok.io', 'http://localhost:5000']

app = Flask(__name__)
CORS(app) #, support_credentials=True)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
# app.config['CORD_HEADERS'] = 'Content-Type'
# conn = sqlite3.connect('moods.db')
# cur = conn.cursor()



# @app.after_request
# def add_cors_headers(response):
#     r = request.referrer[:-1]
#     if r in white:
#         response.headers.add('Accept-Control-Allow-Origin', r)
#         response.headers.add('Accept-Control-Allow-Credentials', 'True')
#         response.headers.add('Accept-Control-Allow-Headers', 'Content-Type')
#         response.headers.add('Accept-Control-Allow-Headers', 'Cache-Control')
#         response.headers.add('Accept-Control-Allow-Headers', 'X-Requested')
#         response.headers.add('Accept-Control-Allow-Headers', 'Authorization')
#         response.headers.add('Accept-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
#     return response

@app.route("/foto", methods=['POST'])
def foto():
    id = int(request.get_json()['id'])
    sqlite_select_query = """SELECT * from moods where moodsid = ?"""
    conn = sqlite3.connect('moods.db', check_same_thread=False)
    cur = conn.cursor()
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


@app.route("/stats", methods=['GET', 'POST'])
def stats():
    id = int(request.args.get('id'))
    conn = sqlite3.connect('moods.db', check_same_thread=False)
    cur = conn.cursor()
    cur.execute("SELECT * FROM moods")
    res = cur.fetchall()
    b = []
    a = []
    g = -1
    for i in res:
        if -i[0] in b:
            print(i)
            a[g].append([i[1], i[2], i[3], i[4]])
        else:
            print(i)
            b.append(-i[0])
            a.append([[i[1], i[2], i[3], i[4]]])
            g+=1
    mol = {b[i]: a[i] for i in range(g+1)}
    print(mol[id])
    res = mol[id]
    pos = neg = net = ''
    result = {
        "pos": [],
        "neg": [],
        "net": []
    }
    for i in res:
        if '0' != i[0]:
            pos += str(i[0]) + ' '
            result["pos"].append(str(i[0]))
        elif '0' != i[1]:
            neg += str(i[1]) + ' '
            result["neg"].append(str(i[1]))
        else:
            net += str(i[3]) + ' '
            result["net"].append(str(i[3]))
    return jsonify(result)



@app.route("/get_brands", methods=['GET'])
def get_brands():
    conn = sqlite3.connect('moods.db', check_same_thread=False)
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