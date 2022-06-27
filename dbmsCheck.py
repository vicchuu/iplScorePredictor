# import pymongo
# import certifi
# #ca = certifi.where()
# from pymongo import MongoClient
#
# cluster = MongoClient("mongodb+srv://vishnuvellimalai:232325@cluster0.94wpmov.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())
# database = cluster["school"]
#
# collect = database["student"]
#
# collect.delete_many({})
#
# dct1 = {"name":"gokka makka", "age":29,"country":"india"}
# dct2 = {"_id":23,"name":"Meera", "age":9,"country":"France"}
# dct3 = {"_id":24,"name":"loki", "age":70,"country":"india"}
# dct4 = {"_id":25,"name":"Vikram", "age":9,"country":"France"}
#
#
# collect.insert_many([dct1,dct2,dct3,dct4])
#
#
# collect.update_many({"_id":5,"_id":23} , {"$set":{"name":"venna mavanae", "age":100,"social_staus":"free_bird"}})
#
# d = collect.find({})
# #print(d)
#
# for c in collect.find():
#     print(c)
#
# #print(c=collect.find())
#
# for c in collect.find({"_id":100}):
#     print(len(c))
#
# #query document , $lt , $in , $gt
#
# print("*****")
# for c in collect.find({"age":{"con$gt":71}}):
#     print(c["name"])
#
#

"""My SQL will start from here"""
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

