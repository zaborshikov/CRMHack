import creds
import parser
import json
class Api:
    def create(shortname):
        result = creds.vk.groups.getById(group_ids=shortname, group_id=shortname)
        id_company = str(result[0]['id'])
        return("-" + id_company)
    def stats(id_company):
        return(object_array)
        #статистика компании
    def comments_analyze(id_company):
        return(plus_array, minus_array, photos)
        #возвращаем хорошие и плохие комменты, плюс фотки к постам
    def get_brands(self):
        return(ids, brands)
        #возврат айди и названия брендов