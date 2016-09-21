from flask import Flask, render_template, request, flash
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField,HiddenField
from wtforms.validators import DataRequired

from DomainModel import db,Campus

campus = Blueprint('campus', __name__)

class CampusForm(Form):
	id = HiddenField('id')
	sigla = StringField('Sigla', validators=[DataRequired()])
	nome = StringField('Campus', validators=[DataRequired()])
	
@campus.route('/listar/')
def campusListar():
	campi = Campus.query.all()
	return render_template('listarCampus.html',listagem = campi)
  
@campus.route('/editar/<int:id>',methods=('GET','POST'))
def CampusEditar(id=0):
	
	if id == 0:
		campus = Campus()
		campus.id = 0
	else:
		campus = Campus.query.filter(Campus.id == id).first()
	
	if request.method == 'POST':
		form = CampusForm(formdata=request.form)
		
		if form.validate():
			form.populate_obj(campus)
			db.session.add(campus)
			db.session.commit()
			flash('New entry was successfully posted') 
	else:
		form = CampusForm(obj=campus)
		
		
	return render_template('editarCampus.html',form=form)
	
@campus.route('/remover/<int:id>',methods=('GET','POST'))
def CampusRemover(id):
	campus = Campus.query.filter(Campus.id == id).first()
	db.session.delete(campus)
	db.session.commit()
	campi = Campus.query.all()
	return render_template('listarCampus.html',listagem = campi)
	
