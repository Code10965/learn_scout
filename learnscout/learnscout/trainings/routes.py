from flask import render_template, url_for, flash, redirect, Blueprint
from flask_login import login_user, current_user #under construction
from learnscout import db #under construction
from learnscout.models import User, Function, Training #under construction
from learnscout.users.forms import LoginForm
from learnscout.trainings import db_connect_dropdown as dropdown, db_connect_traininglist as traininglist

trainings = Blueprint('trainings', __name__)

@trainings.route('/getguidance' , methods=['GET', 'POST'])
def getguidance():
    form=LoginForm()
    return render_template('getguidance.html', title='Get Guidance', form=form, functions=dropdown.get_data(), training=traininglist.get_training())

def update_function():
    form=LoginForm()
    if form.validate_on_submit():
        newfunction = request.form.get("selected_function")
        oldfunction = request.form.get("empty_function")
        update = User.query.filter_by(username=current_user.username).first()
        update.function_selected = newfunction
        db.session.commit()
        location.reload
    return render_template('myupskillingplan.html', title='Get Guidance', form=form, functions=dropdown.get_data(), training=traininglist.get_training())

@trainings.route('/myupskillingplan')
def myupskillingplan():
    return render_template('myupskillingplan.html', title='My Upskilling Plan')

@trainings.route('/startupskilling')
def startupskilling():
    return render_template('startupskilling.html', title='Start Upskilling')

@trainings.route('/material')
def material():
    return render_template('material.html', title='Material for Upskilling')
