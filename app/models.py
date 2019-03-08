from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    tlf = db.Column(db.Integer, unique=True)
    sex = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    trips = db.relationship('UserTrips', backref='owner', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class UserTrips(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(250))
    time = db.Column(db.Date, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'))


class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trips = db.relationship('UserTrips', backref='TripRoute', lazy='dynamic')

