# encoding:utf-8
# author:wwg
from flask import *
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import *
from wtforms.validators import ValidationError

class NameForm(Form):
    name=StringField('your name',validators=[Required()])
    password=StringField('your password',validators=[Required()])
    submit=SubmitField('submit')
