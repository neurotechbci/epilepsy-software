# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField,DecimalField
from wtforms.validators import InputRequired, Email, DataRequired

## login and registration

class CreatePatientForm(FlaskForm):
    username = TextField('Username'     , id='username_create' , validators=[DataRequired()])
    email    = TextField('Email'        , id='email_create'    , validators=[DataRequired(), Email()])
    id = DecimalField('ID'     , id='id' , validators=[DataRequired()])
    age = DecimalField('Age'     , id='age' , validators=[DataRequired()])