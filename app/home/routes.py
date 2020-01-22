# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from flask import render_template, redirect, url_for , request
from flask_login import login_required, current_user
from app import login_manager,db
from jinja2 import TemplateNotFound
from app.home.models import Patient
from app.home.forms import CreatePatientForm

@blueprint.route('/index',methods=['GET','POST'])
@login_required
def index():
    msg = ""
    print(request.form)
    create_patient_form = CreatePatientForm(request.form)
    if 'create_patient' in request.form:
        username = request.form['username']
        age = request.form['age']
        email = request.form['email']
        id = request.form['id']
        patient = Patient.query.filter_by(id=id).first()
        if patient:
            msg= "Already registered"
        else:
            msg = "To register"
            patient = Patient(**request.form)
            db.session.add(patient)
            db.session.commit()

    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))
    
    patients = db.session.query(Patient)

    return render_template('index.html',form = create_patient_form,patients=patients,msg=msg)

@blueprint.route('/<template>')
def route_template(template):

    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))

    try:

        return render_template(template + '.html')

    except TemplateNotFound:
        return render_template('error-404.html'), 404
    
    except:
        return render_template('error-500.html'), 500
