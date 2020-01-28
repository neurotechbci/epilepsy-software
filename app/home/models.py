# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from app import db
from sqlalchemy import Binary, Column, Integer, String , DateTime
from sqlalchemy.orm import relationship,backref


class Patient(db.Model):

    __tablename__ = 'Patient'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    age = Column(Integer, unique=False)
    visits = Column(Integer, unique=False,default = 1)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)

class PatientVisitDetails(db.Model):

    __tablename__ = 'PatientVisitDetails'

    visit_id = Column(Integer,primary_key = True)
    patient_id = Column(Integer)
    date_time = Column(DateTime, unique = False)
    doctor_id = Column(Integer)
    questionnaires = relationship('PatientVisitDetails',backref='question')

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            setattr(self, property, value)

    def __repr__(self):
        return str(self.visit_id)

class Questionnaire(db.Model):

    __tablename__ = 'Questionnaire'
    
    question_1 = Column(String)
    question_2 = Column(String)
    question_3 = Column(String)
    question_4 = Column(String)
    question_5 = Column(String)
    question_6 = Column(String)
    questionnaire_id = Column(Integer,primary_key=True)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            setattr(self, property, value)

    def __repr__(self):
        return str(self.visit_id)