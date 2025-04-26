from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))
    email = db.Column(db.String(32))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    body = db.Column(db.String(256))
    # timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    # def __repr__(self):
    #  return '<Posts {}>'.format(self.body)

# class Age(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     age = db.Column(db.String(32))


    
