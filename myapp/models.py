from .extensions import db 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))

class Account(db.Model):
    account_id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.numeric(12,2))