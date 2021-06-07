from datetime import datetime
from blog import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')


    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_title = db.Column(db.String(500))
    description = db.Column(db.String(2000))
    body = db.Column(db.String(20000))
    post_url = db.Column(db.String(140))
    category = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    featured = db.Column(db.Boolean)
    # categories = {'mathsci':'Math + Science', 'eng':'Tech + Code', 'artlit':'Art and Literature', 'other':'Other'}


    def __repr__(self):
        return '<Post {}>'.format(self.post_title)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))