from flask import render_template, url_for, flash, redirect
from learnscout import app, db, bcrypt
from learnscout.forms import RegistrationForm, LoginForm
from learnscout.models import User, Function, Training
from flask_login import login_user, current_user


@app.route('/' ,)
@app.route('/welcome',)
@app.route('/learnscout',)
@app.route('/logout' ,)
def welcome():
    return render_template('welcome.html', title='Welcome')



@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password )
        db.session.add(user)
        db.session.commit()
        flash(f"Thank you, {form.username.data.title()}. Your account has been created successfully,  . . .")
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash (f", your login was successful.")
            return redirect(url_for('getguidance'))

        else:
            flash ("Login not successful. Please check you email and password.")
    return render_template('login.html', title='Login', form=form)

@app.route('/getguidance' , methods=['GET', 'POST'])
def getguidance():
    return render_template('getguidance.html', title='Get Guidance')

@app.route('/myupskillingplan')
def myupskillingplan():
    return render_template('myupskillingplan.html', title='My Upskilling Plan')

@app.route('/startupskilling')
def startupskilling():
    return render_template('startupskilling.html', title='Start Upskilling')

@app.route('/material')
def material():
    return render_template('material.html', title='Material for Upskilling')
