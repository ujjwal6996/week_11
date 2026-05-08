from flask_sqlalchemy import SQLAlchemy
# we dont import app here

db=SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20),nullable=False,unique=True)
    password=db.Column(db.String(20),nullable=False)
    roles=db.relationship('Role',backref='users',secondary='association')#parent hai User

class Role(db.Model):#sibling
    id = db.Column(db.Integer,primary_key=True)
    role_name=db.Column(db.String(),nullable=False,unique=True)

class Association(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    role_id=db.Column(db.Integer,db.ForeignKey('role.id'),nullable=False)