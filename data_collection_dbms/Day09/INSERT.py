import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "root",
    database = "classwork_db"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO emp(ename,sal) VALUES(%s,%s)",("rohan",2000))
mycursor.close()
mydb.commit()
mydb.close()