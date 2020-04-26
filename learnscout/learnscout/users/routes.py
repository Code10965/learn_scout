from flask import render_template, url_for, flash, redirect, Blueprint
from flask_login import login_user, current_user
from learnscout import db, bcrypt
from learnscout.models import User, Function, Training 
from learnscout.users.forms import RegistrationForm, LoginForm 

users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password )
        db.session.add(user)
        db.session.commit()
        flash(f"Thank you, {form.username.data.title()}. Your account has been created successfully,  . . .")
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash (f", your login was successful.")
            return redirect(url_for('trainings.getguidance'))

        else:
            flash ("Login not successful. Please check you email and password.")
    return render_template('login.html', title='Login', form=form)



