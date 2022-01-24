from datetime import datetime
from sayhello import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(300))
    ip = db.Column(db.String(30))
    iname = db.Column(db.String(10))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    comments = db.relationship('Comment', backref='post', cascade='all')


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(100))
    iname = db.Column(db.String(10))
    ip = db.Column(db.String(30))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'))
    message = db.relationship('Message', back_populates='comments')