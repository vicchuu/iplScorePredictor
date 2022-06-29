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

# import mysql.connector #conda install mysql-python
# import json
# from flask_mysql import MySQL
#
# from flask import Flask,render_template, request
# from flask_mysqldb import MySQL
#
# app = Flask(__name__)
#
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'flask'
#
# mysql = MySQL(app)

import mysql.connector
try:
  db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="rootvishnu",
  database ="testdb"
  )
except:
  print("issue in connectivity")

my_cursor = db_connection.cursor()
my_cursor.execute("DELETE FROM student")
#CREATE DATABASE NAME
#my_cursor.execute("REMOVE DATABASE testdb")

#printing availabel data bases
#my_cursor.execute("show databases")
#print(db_connection.cursor().execute("show databases"))
# my_cursor.execute("SHOW TABLES")


# def reverse(nums):
#     return [nums[-1]]+reverse(nums[:-1]) if nums else []
#
# #backwards = lambda l: (backwards (l[1:]) + l[:1] if l else [])
#
# backwards =  lambda  nums : (backwards( nums[1:]) + nums[:1] if nums else [])
#
#
# a = [9,23,4,2,11,5,25,6]
# [ print(a[i],end= " ") for i  in range(len(a)-1,-1,-1)]
#
# print(backwards(a))
#print(c)


#creating a table

#my_cursor.execute("CREATE TABLE student (name VARCHAR(255),age INTEGER(10), marks INTEGER(10))")



insert_values = "INSERT INTO student (name ,age,marks,gender) VALUES (%s,%s,%s,%s)"

student1 = [("Vishnu" , 29,93 ,"Male"),
            ("alpha1" , 19,93,"M"),
            ("beta2" , 39,93,"M"),
            ("game3" , 49,93,"M"),
            ("Radii4" , 59,93,"F")]
#
my_cursor.executemany(insert_values,student1)

#

#my_cursor.execute("SELECT * FROM student  WHERE name LIKE '%s%'")
#my_cursor.execute("SELECT * FROM student ORDER BY name ASC")

# updating existing value in SQl

#my_cursor.execute("UPDATE student SET age = 0000000009 WHERE name ='vishnu' ")
my_cursor.execute("SELECT * FROM student ")

#my_cursor.execute("ALTER TABLE student ADD gender VARCHAR(6) NOT NULL")
#my_cursor.execute("ALTER TABLE student RENAME TO students")
my_cursor.execute("ALTER TABLE student MODIFY gender VARCHAR(5)")
#my_cursor.execute("DESCRIBE student")

result = my_cursor.fetchall()
for i in result:
   print(i)
#
db_connection.commit()


