import sqlite3 

connection = sqlite3.connect("animals.db")
cursor = connection.cursor()
cursor.execute("select * from pets")
result = cursor.fetchall()

print(result)
