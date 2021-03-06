from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from geoalchemy2.types import Geography

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
    trips = db.relationship('Trips', backref='owner', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Tracks(db.Model):
    __tablename__ = 'tracks'
    gid = db.Column(db.Integer, primary_key=True)
    rutenavn = db.Column(db.String(33))
    rutenummer = db.Column(db.String(13))
    spes_fotru = db.Column(db.String(2))
    gradering = db.Column(db.String(1))
    rutemerkin = db.Column(db.String(3))
    rutefolger = db.Column(db.String(2))
    oppdatdato = db.Column(db.String(20))
    belysning = db.Column(db.SMALLINT)
    lokalid = db.Column(db.String(100))
    navnerom = db.Column(db.String(100))
    noyaktighe = db.Column(db.INTEGER)
    synbarhet = db.Column(db.SMALLINT)
    objtype = db.Column(db.String(32))
    skilting = db.Column(db.String(3))
    rutebetydn = db.Column(db.SMALLINT)
    geog = db.Column(Geography(geometry_type='LINESTRING'))
    trips = db.relationship('Trips', backref='Triptrack', lazy='dynamic')

    def __repr__(self):
        return '{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}'.format(self.gid, self.rutenavn, self.rutenummer, self.spes_fotru, self.gradering, self.rutemerkin, self.rutefolger, self.oppdatdato, self.belysning, self.lokalid, self.navnerom, self.noyaktighe, self.synbarhet, self.objtype, self.skilting, self.rutebetydn, self.geog)




class Trips(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(250))
    time = db.Column(db.Date, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.gid'))
