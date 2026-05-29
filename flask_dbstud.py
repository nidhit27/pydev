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

@app.route('/')
def login():

    uname = request.args.get("uname")
    psw = request.args.get("psw")

    ##mycursor = mydb.cursor()

    sql = "SELECT * FROM students WHERE Name=%s AND City=%s"

    values = (uname, psw)

    mycursor.execute(sql, values)

    result = mycursor.fetchone()

    mycursor.close()

    if result:
        return "Student is in Database"
    else:
        return "Student Not Found"



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
        line=str(row[0]) +  " " + str(row[1]) + " " + str(row[2]) + "<br>"
        st += line
        print(st)
    mycursor.close()
    return st
