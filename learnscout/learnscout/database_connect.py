"""import sqlite3

db_connection = sqlite3.connect('learnscout\learnscout\site.db')

db_cursor = db_connection.cursor()
 
db_cursor.execute("SELECT * FROM site")

list_function = db_cursor.fetchall()

print(list_function)


db_connection.close()
"""