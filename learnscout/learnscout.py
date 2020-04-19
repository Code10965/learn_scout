from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchenmy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ba8eb8f0064b4745fe689f9fde30c3ac'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchenmy(app)

subs=db.Table('subs',
     db.Column('user_id', db.Integer,db.ForeignKey('user.user_id')),
     db.Column('training_id',db.Integer,db.ForeignKey('training.training_id')),
     )

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    function = db.Column(db.String(100), nullable=False, default="team-member")
    skill = db.Column(db.String(100), nullable=False, default="team-skill")
    status = db.Column(db.BIT(1), nullable=False, default="0")
    subscriptions = db.relationship('Training', secondary=subs, backref=db.backref('participant', lazy='True'))

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.function}')"

class Training(db.Model):
    training_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.String(100), unique=True, nullable=False)



    def __repr__(self):
        return f"Plan('{self.selected_skill}', '{self.selected_done}')"

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
        flash(f"Account created for {form.username.data}.")
        return redirect(url_for('get_guidance'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data =='admin@learnscout.com' and form.password.data == 'password':
            flash ("You have been looged in.")
            return redirect(url_for('get_guidance'))
        else: flash ("Login not successful. Please check you email and password.")
    return render_template('login.html', title='Login', form=form)

@app.route('/getguidance' , methods=['GET', 'POST'])
def get_guidance():
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

if __name__ == '__main__':
    app.run(debug=True)
