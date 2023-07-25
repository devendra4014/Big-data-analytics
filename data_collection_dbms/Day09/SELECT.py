import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "root",
    database = "classwork_db"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM emp")
result = mycursor.fetchall()
mycursor.close()

for obj in result:
    print(obj)