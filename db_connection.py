"""
user: root
password: qwerty
host: 127.0.0.1
port: 3306
database: starwarsDB
"""

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(
    host="127.0.0.1",
    user="root",
    port=3306,
    password="Ankit@123",
    database="starwarsDB",
    cursorclass=pymysql.cursors.DictCursor,
)

cursor = connection.cursor()
cursor.execute("SHOW DATABASES")
results = cursor.fetchall()
for result in results:
    print(result)
