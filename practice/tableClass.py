# encoding:utf-8
# author:wwg
from flask_sqlalchemy import SQLAlchemy
from flask import *
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  "mysql://root:123abc@localhost/test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64))
    password=db.Column(db.String(128))

