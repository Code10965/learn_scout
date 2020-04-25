from learnscout import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    function_selected = db.Column(db.String(100), nullable=False, default="TBD")

    def __repr__(self):
        return f"('{self.username}', '{self.email}', '{self.function_selected}')"

class Function(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    functionname = db.Column(db.String(100), unique=True, nullable=False)
    skill_1 = db.Column(db.String(100), nullable=True)
    skill_2 = db.Column(db.String(100), nullable=True)
    skill_3 = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"Function('{self.functionname}', '{self.skill_1}', '{self.skill_2}' , '{self.skill_3}')"

class Training(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trainingname = db.Column(db.String(100), unique=True, nullable=False)
    signed_up = db.Column(db.String(25), nullable=True)
    participant = db.Column(db.String(25), nullable=True)
    material = db.Column(db.String(100), unique=True, nullable=True)

    def __repr__(self):
        return f"Training('{self.trainingname}', '{self.signed_up}', '{self.participant}')"
