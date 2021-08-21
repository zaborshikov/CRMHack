from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
app = Flask(__name__)
api = Api(app)


class Api():
    def create(self, vk_link):
        return(id_company)
    def stats(self, id_company):
        return(object_array)
        #статистика компании
    def comments_analyze(self, id_company):
        return(plus_array, minus_array, photos)
        #возвращаем хорошие и плохие комменты, плюс фотки к постам
    def get_brands(self):
        return(ids, brands)
        #возврат айди и названия брендов