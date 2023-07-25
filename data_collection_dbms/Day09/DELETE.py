import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "root",
    database = "classwork_db"
)

mycursor = mydb.cursor()

mycursor.execute("DELETE FROM emp WHERE empno = %s",(1,))
mycursor.close()
mydb.commit()
mydb.close()