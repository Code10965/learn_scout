from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from learnscout.config import Config 


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view ='users.login'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from learnscout.users.routes import users 
    from learnscout.trainings.routes import trainings 
    #from learnscout.functions.routes import functions 
    from learnscout.main.routes import main 
    app.register_blueprint(users)
    app.register_blueprint(trainings)
    #app.register_blueprint(functions)
    app.register_blueprint(main)

    return app