import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="nidhi",
  password="nidhi123",
  database="studentrep"
)
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


print("-----")

mycursor.execute("select * from students")

for x in mycursor:
  print(x)

print("-----")

mycursor.execute("select * from teachers")

for x in mycursor:
  print(x)

mycursor.close()

