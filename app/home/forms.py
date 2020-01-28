# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField,DecimalField,DateTimeField,DateField,TextAreaField
from wtforms.validators import InputRequired, Email, DataRequired
from wtforms.fields.html5 import DateTimeLocalField

## login and registration

class CreatePatientForm(FlaskForm):
    username = TextField('Username'     , id='username_create' , validators=[DataRequired()])
    email    = TextField('Email'        , id='email_create'    , validators=[DataRequired(), Email()])
    id = DecimalField('Id'     , id='id' , validators=[DataRequired()])
    age = DecimalField('Age'     , id='age' , validators=[DataRequired()])

class CreateVisitForm(FlaskForm):
    visit_datetime = DateTimeLocalField('Which date is your favorite?', format='%m/%d/%y', validators=[DataRequired()])
    doctor_id = DecimalField('Doctor ID '     , id='doctor_id' , validators=[DataRequired()])

class QuestionnaireForm(FlaskForm):
    question_1 = TextAreaField('This is the question 1. Please fill up the details necessary',id='question_1')
    question_2 = TextAreaField('This is the question 2. Please fill up the details necessary',id='question_2')
    question_3 = TextAreaField('This is the question 3. Please fill up the details necessary',id='question_3')
    question_4 = TextAreaField('This is the question 4. Please fill up the details necessary',id='question_4')
    question_5 = TextAreaField('This is the question 5. Please fill up the details necessary',id='question_5')
    question_6 = TextAreaField('This is the question 6. Please fill up the details necessary',id='question_6')