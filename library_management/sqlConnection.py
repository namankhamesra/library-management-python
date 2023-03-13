import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger"
)
myCursor = mydb.cursor()
try:
    myCursor.execute("create database if not exists library;")
except Exception as e:
    print(e)
else:
    myCursor.execute("use library")