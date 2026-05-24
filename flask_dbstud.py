from flask import Flask, request
import mysql.connector
app = Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="nidhi",
  password="nidhi123",
  database="studentrep"
)
mycursor = mydb.cursor()

@app.route('/students')
def stu():
    mycursor.execute("select * from students")
    results = mycursor.fetchall()
    st = " "
    for row in results:
        line=str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + "<br>"
        st += line
        print(st)
    mycursor.close()
    return st



   

@app.route('/teachers')
def tea():
    mycursor.execute("select * from teachers")
    results = mycursor.fetchall()
    st = " "
    for row in results:
        line=str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + "<br>"
        st += line
        print(st)
    mycursor.close()
    return st
