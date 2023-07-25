#!/usr/bin/python

from pyhive import hive

# hive config
host_name = 'localhost'
port = 10000
user = 'nilesh'
password = ''
db_name = 'dbda'

# get hive connection
conn = hive.Connection(host=host_name, port=port, username=user, password=password, database=db_name, auth='CUSTOM')

# get the cursor object
cur = conn.cursor()

# execute the sql query using cursor
id = input('enter id: ')
sql = "SELECT * FROM books WHERE id=" + id
cur.execute(sql)

# collect/process result
result = cur.fetchall()
for row in result:
    print(row)

# close the connection
conn.close()

#### Execution
# Run1: Input id = 1001
    # SELECT * FROM books WHERE id=1001
# Run2: Input id = 1001 OR true (SQL Injection demo)
    # SELECT * FROM books WHERE id=1001 OR true

