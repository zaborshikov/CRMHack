import sqlite3
import creds
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/create", methods=['GET', 'POST'])
def create(shortname):
    if request.method == 'POST':
        try:
            sqlite_connection = sqlite3.connect('moods.db')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")

            sqlite_select_query = """SELECT * from moods where moodsid = ?"""
            cursor.execute(sqlite_select_query, (id, ))
            print("Чтение одной строки \n")
            records = cursor.fetchmany(all)
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
    else:
        pass
@app.route("/comment_analyse", methods=['GET', 'POST'])
def comment_analyse(id):
    if request.method == 'GET':
        try:
            sqlite_connection = sqlite3.connect('moods.db')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")

            sqlite_select_query = """SELECT * from moods where moodsid = ?"""
            cursor.execute(sqlite_select_query, (id))
            print("Чтение одной строки \n")
            record = cursor.fetchone()
            print(record[0])
            print(record[1])
            print(record[2])
            print(record[3])
            print(record[4])

            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("Соединение с SQLite закрыто")
            return pos, neg, photos, posts
    else:
        pass
# def create(shortname):
#     result = creds.vk.groups.getById(group_ids=shortname, group_id=shortname)
#     id_company = str(result[0]['id'])
#     return("-" + id_company)

conn = sqlite3.connect('moods.db')
cur = conn.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS moods(
#     moodsid INT PRIMARY KEY,
#     positive TEXT,
#     negative TEXT);""")
    # def stats(id_company):
    #     return(object_array)
    #     #статистика компании
    # def comments_analyze(id_company):
    #     return(plus_array, minus_array, photos)
    #     #возвращаем хорошие и плохие комменты, плюс фотки к постам
    # def get_brands(self):
    #     return(ids, brands)
    #     #возврат айди и названия брендов
class Database:
    def create(shortname):
        result = creds.vk.groups.getById(group_ids=shortname, group_id=shortname)
        id_company = str(result[0]['id'])
        return("-" + id_company)
    def setPos(id, positive, message):
        print(message)
        cur.execute(f"insert into moods (positive, moodsid, comment) values ({positive}, {id}, '{message}')")
        # except Exception:
        #     print(Exception)
        conn.commit()

    def setNeg(id, negative, message):
        cur.execute(f"insert into moods (negative, moodsid, comment) values ({negative}, {id}, '{message}')")
        # except Exception:
        #     print(Exception)
        conn.commit()
    def setNeutral(id, neutral, message):
        cur.execute(f"insert into moods (neutral, moodsid, comment) values ({neutral}, {id}, '{message}')")

    def getIDs():
        cur.execute("SELECT * FROM companyid")
        res = cur.fetchone()
        return(res)
        # except Exception:
        #     print(Exception)

    def getMood():
        cur.execute("SELECT * FROM moods")
        res = cur.fetchone()
        return res
        # except Exception:
        #     print(Exception)
    def comment_analyse(id):
        try:
            sqlite_connection = sqlite3.connect('moods.db')
            cursor = sqlite_connection.cursor()
            print("Подключен к SQLite")

            sqlite_select_query = """SELECT * from moods where moodsid = ?"""
            cursor.execute(sqlite_select_query, (id, ))
            print("Чтение одной строки \n")
            records = cursor.fetchmany(all)
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