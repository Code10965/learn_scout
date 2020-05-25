import sqlite3
# for getting the dropdown menu content from the database
def get_data():
    db_connection = sqlite3.connect('learnscout/site.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute("SELECT * FROM function")
    list_function = db_cursor.fetchall()
    functions_listed = []
    for i in range(0,len(list_function)):
        x=list_function.pop(0)
        y=str(x[1])
        functions_listed.append(y)
    final_list = functions_listed
    db_connection.close()
    return(final_list)
