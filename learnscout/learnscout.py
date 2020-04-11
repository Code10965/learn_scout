from flask import Flask
app = Flask(__name__)


@app.route('/')
def welcome():
    return '<h1>hednwuencllo world</h1>'

@app.route('/getguidance')
def get_guidance():
    return '<h1>Get Guidance</h1>'

@app.route('/login')
@app.route('/logout')
def login():
    return '<h1>Please log-in here</h1>'


if __name__ == '__main__':
    app.run(debug=True)