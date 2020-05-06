from flask_login import current_user
import sqlite3

# for updating the function of user in user table
def function_update():
    db_connection = sqlite3.connect('learnscout/site.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute("UPDATE user SET function_selected= option_selected WHERE username = current_user.username")



    list_function = db_cursor.fetchall()
    functions_listed = []
    for i in range(0,len(list_function)):
        x=list_function.pop(0)
        y=str(x[1])
        functions_listed.append(y)
    final_list = functions_listed
    db_connection.close()
    return(final_list)




db_connection = sqlite3.connect('learnscout\learnscout\site.db')

db_cursor = db_connection.cursor()
 
db_cursor.execute("UPDATE user SET function_selected= option_selected WHERE username = current_user.username")

db_connection.close()
