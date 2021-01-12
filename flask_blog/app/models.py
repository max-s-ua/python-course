from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
from flask_login import UserMixin

likes = db.Table('likes',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('article_id', db.Integer, db.ForeignKey('article.id')),
    db.Column('like', db.Boolean, default=True)        
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Article', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    #likes = db.relationship('User', secondary=likes, backref=db.backref('likes',lazy='dynamic'))
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def avatar(self, size):
        avacode = md5(self.email.encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&=s={}'.format(avacode, size)

    def followed_posts(self):
        return Article.query.filter_by(user_id=self.id).order_by(Article.created_at.desc()).all()

    
    def __repr__(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.String(1000))
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    edited_at = db.Column(db.DateTime, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    likes = db.relationship('User', secondary=likes, backref=db.backref('likes',lazy='dynamic'))

    def liked_by_user(self, user):
        return user in self.likes

    def get_likes_count(self):
        return len(self.likes)

    def get_create_time(self):
        return self.created_at.strftime('%d.%m.%y - %H:%M')

    def __repr__(self):
        return '<Article {}>'.format(self.title)
