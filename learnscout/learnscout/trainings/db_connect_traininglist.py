import sqlite3
from flask_login import current_user
from learnscout.models import User
# for getting the dropdown menu content from the database

def get_training():
    user = User.query.filter_by(function_selected=current_user.function_selected).first()
    db_connection = sqlite3.connect('learnscout/site.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute("SELECT training.for_function, training.trainingname FROM training INNER JOIN user ON training.for_function = user.function_selected")
    list_training = db_cursor.fetchall()
    
    trainings_listed = []
    for i in range(0,len(list_training)):
        x=list_training.pop(0)
        y=(x[0])
        z=(x[1])
        if y == current_user.function_selected:
            trainings_listed.append(z)
    final_list = trainings_listed
    db_connection.close()
    return(final_list)
"""
db_connection = sqlite3.connect('learnscout/site.db')
db_cursor = db_connection.cursor()
db_cursor.execute("SELECT training.for_function, training.trainingname FROM training INNER JOIN user ON training.for_function = user.function_selected")
list_training = db_cursor.fetchall()

trainings_listed = []
for i in range(0,len(list_training)):
    x=list_training.pop(0)
    y=(x[0])
    z=(x[1])
    if y == "Planning":
        trainings_listed.append(z)
final_list = trainings_listed
db_connection.close()
print(final_list)
"""