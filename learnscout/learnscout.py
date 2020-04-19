from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ba8eb8f0064b4745fe689f9fde30c3ac'

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/' , methods=['GET', 'POST'])
@app.route('/welcome', methods=['GET', 'POST'])
@app.route('/learnscout', methods=['GET', 'POST'])
@app.route('/logout' , methods=['GET', 'POST'])
def welcome():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}.")
        return redirect(url_for('get_guidance'))
    return render_template('welcome.html', title='Welcome', form=form)

@app.route('/testpage', methods=['GET', 'POST'])
def testpage():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}.")
        return redirect(url_for('get_guidance'))
    return render_template('testpage.html', title='Testpage', form=form)

    form=LoginForm()
    if form.validate_on_submit():
        flash(f"Welcome to learnscout, {form.username.data}.")
        return redirect(url_for('get_guidance'))
    return render_template('testpage.html', title='Testpage', form=form)

@app.route('/getguidance' , methods=['GET', 'POST'])
def get_guidance():
    return render_template('getguidance.html', title='Get Guidance')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}.")
        return redirect(url_for('get_guidance'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('get_guidance'))
    return render_template('login.html', title='Login', form=form)

@app.route('/myupskillingplan')
def myupskillingplan():
    return render_template('myupskillingplan.html', title='My Upskilling Plan')

@app.route('/startupskilling')
def startupskilling():
    return render_template('startupskilling.html', title='Start Upskilling')

@app.route('/material')
def material():
    return render_template('material.html', title='Material for Upskilling')

if __name__ == '__main__':
    app.run(debug=True)
