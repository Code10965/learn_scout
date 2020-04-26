from flask import render_template, Blueprint 

main = Blueprint('main', __name__)

@main.route('/' ,)
@main.route('/welcome',)
@main.route('/learnscout',)
@main.route('/logout' ,)
def welcome():
    return render_template('welcome.html', title='Welcome')
