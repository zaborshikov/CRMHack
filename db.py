import sqlite3
import datetime
import creds

class DataBase:
    def __init__(self):
        self.db = sqlite3.connect("../db/users.db")
        self.sql = self.db.cursor()
        try:
            self.sql.execute("""CREATE TABLE users
                                  (id, mark, date)
                               """)
        except Exception as e:
            print(e, 14)

        try:
            self.sql.execute("""CREATE TABLE message
                                  (id, text, ans INT)
                               """)
        except Exception as e:
            print(e, 21)
        try:
            self.sql.execute("""CREATE TABLE matrix
                                  (id, param1, param2, param3, positive, negative, neutral)
                               """)
        except Exception as e:
            print(e, 27)

    def AddUser(self, userID):
        self.sql.execute(f""" SELECT id FROM users WHERE id = {userID} """)
        if self.sql.fetchone() is None:
            # self.sql.execute("SELECT id FROM users")
            self.sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (userID, 0, datetime.date.today()))
        self.db.commit()
    
    def create(shortname):
        result = creds.vk.groups.getById(group_ids=shortname, group_id=shortname)
        id_company = str(result[0]['id'])
        return("-" + id_company)

    def setData(self, DateID, date):
        try:
            self.sql.execute(f'SELECT id FROM users WHERE id = "{DateID}" ')
            if self.sql.fetchone() is None:
                pass
            else:
                self.sql.execute(f' UPDATE users SET date = "{date}" WHERE id = "{DateID}" ')
        except Exception as e:
            print(e, 44)
        self.db.commit()

    def setAns(self, idAns, ans):
        try:
            self.sql.execute(f'SELECT ans FROM message WHERE id = {idAns} ')
            self.sql.execute(f' UPDATE message SET ans = {ans} WHERE id = {idAns} ')
        except Exception as e:
            print(e, 57)
        self.db.commit()

    def getAns(self, idA):
        try:
            self.sql.execute(f'SELECT ans FROM message WHERE id = {idA} ')
            an = str(self.sql.fetchone())
            an = an.replace('(', '')
            an = an.replace(',', '')
            an = an.replace(')', '')
            try:
                return int(an)
            except Exception as e:
                print(e, 70)
                return 0
        except Exception as e:
            print(e, 73)

    def getAll(self):
        try:
            self.sql.execute(f'SELECT id FROM users')
            AllID = self.sql.fetchall()
            ids = []
            for i in AllID:
                idd = str(i)
                a = idd.replace('(', '')
                b = a.replace(',', '')
                c = b.replace(')', '')
                ids.append(c)
            return ids
        except Exception as e:
            print(e, 88)

    def getText(self):
        self.sql.execute("SELECT u.rowid, u.id, m.text FROM users u LEFT JOIN message m ON m.id = u.id")
        texts = []
        dbTexts = self.sql.fetchall()
        for i, el in enumerate(dbTexts):
            try:
                if dbTexts[i][0] == dbTexts[i + 1][0]:
                    dbTexts.pop(i)
            except Exception as e:
                print(e, 99)
        for el in dbTexts:
            texts.append(str(el[2]))
        return texts

    # message
    def AddMessage(self, idMes, text):
        try:
            self.sql.execute(f"SELECT id FROM message WHERE id = '{idMes}' ")
            if self.sql.fetchone() is None:
                self.sql.execute("SELECT id FROM users")
                self.sql.execute(f"INSERT INTO message VALUES (?, ?, ?)", (idMes, text, -1))
        except Exception as e:
            print(e, 112)
        self.db.commit()

    def AddRes(self, ResID, param1, param2, param3, positive, negative, neutral):
        # self.sql.execute("SELECT rowid, param1, param2, param3 FROM matrix")
        try:
            self.sql.execute(
                f"UPDATE matrix SET param1 = {param1}, param2 = {param2}, param3 = {param3}, positive = {positive}, "
                f"negative = {negative}, neutral = {neutral} WHERE id = {ResID}")
        except Exception as e:
            print(e, 121)
        self.db.commit()

    def setParam1(self, P1ID, param1):
        try:
            self.sql.execute(f"UPDATE matrix SET param1 = {param1} WHERE id = {P1ID}")
        except Exception as e:
            print(e, 128)
        self.db.commit()

    def setParam2(self, P2ID, param2):
        try:
            self.sql.execute(f"UPDATE matrix SET param2 = {param2} WHERE id = {P2ID}")
        except Exception as e:
            print(e, 135)
        self.db.commit()

    def setParam3(self, P3ID, param3):
        try:
            self.sql.execute(f"UPDATE matrix SET param3 = {param3} WHERE id = {P3ID}")
        except Exception as e:
            print(e, 142)
        self.db.commit()

    def setPos(self, PID, positive):
        try:
            self.sql.execute(f"UPDATE matrix SET positive = {positive} WHERE id = {PID}")
        except Exception as e:
            print(e, 149)
        self.db.commit()

    def setNegative(self, NegID, negative):
        try:
            self.sql.execute(f"UPDATE matrix SET negative = {negative} WHERE id = {NegID}")
        except Exception as e:
            print(e, 156)
        self.db.commit()

    def setNeutral(self, NID, neutral):
        try:
            self.sql.execute(f"UPDATE matrix SET neutral = {neutral} WHERE id = {NID}")
        except Exception as e:
            print(e, 163)
        self.db.commit()

    def getMatrix(self):
        self.sql.execute(f" SELECT id, param1, param2, param3, positive, negative, neutral, id FROM matrix")
        mar = self.sql.fetchall()
        return mar

    def AddID(self, MID):
        try:
            self.sql.execute(f"SELECT id FROM matrix WHERE id = {MID}")
            if self.sql.fetchone() is None:
                self.sql.execute(f"INSERT INTO matrix VALUES (?, ?, ?, ?, ?, ?, ?)", (MID, 0, 0, 0, 0, 0, 0))
        except Exception as e:
            print(e, 186)
        self.db.commit()
    def countUsers(self):
        try:
            return(self.sql.execute(f"SELECT count(*) from users"))
        except Exception as e:
            print(e, 189)