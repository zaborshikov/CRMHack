import sqlite3
import datetime
import creds

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
    def setPos(self, id, positive):
        try:
            cur.execute(f"UPDATE moods SET positive = {positive} where id = {id}")
        except Exception:
            print(Exception)
        conn.commit()
    def setNeg(self, id, negative):
        try:
            cur.execute(f"UPDATE moods SET negative = {negative} where id = {id}")
        except Exception:
            print(Exception)
        conn.commit()
    def create(shortname):
        result = creds.vk.groups.getById(group_ids=shortname, group_id=shortname)
        id_company = str(result[0]['id'])
        return("-" + id_company)
