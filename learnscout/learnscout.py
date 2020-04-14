from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
@app.route('/welcome')
@app.route('/learnscout')
@app.route('/logout')
def welcome():
    return render_template('welcome.html')

@app.route('/getguidance')
def get_guidance():
    return render_template('getguidance.html', title='Get Guidance')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

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