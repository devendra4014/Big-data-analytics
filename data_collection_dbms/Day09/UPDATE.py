import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "root",
    database = "classwork_db"
)

mycursor = mydb.cursor()

mycursor.execute("UPDATE emp SET empno = %s WHERE ename = %s",(1,"rohan"))
mycursor.close()
mydb.commit()
mydb.close()