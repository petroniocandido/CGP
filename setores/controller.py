from flask import Flask, render_template, request, flash
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField,HiddenField
from wtforms.validators import DataRequired

from DomainModel import db,Setor

setores = Blueprint('setores', __name__)

class SetorForm(Form):
	id = HiddenField('id')
	sigla = StringField('Sigla', validators=[DataRequired()])
	nome = StringField('Setor', validators=[DataRequired()])
	telefone = StringField('Telefone')
	
@setores.route('/listar/')
def setoresListar():
	setores = Setor.query.all()
	return render_template('listarSetores.html',setores = setores)
  
@setores.route('/editar/<int:id>',methods=('GET','POST'))
def setorEditar(id=0):
	
	if id == 0:
		setor = Setor()
		setor.id = 0
	else:
		setor = Setor.query.filter(Setor.id == id).first()
	
	if request.method == 'POST':
		form = SetorForm(formdata=request.form)
		
		if form.validate():
			form.populate_obj(setor)
			db.session.add(setor)
			db.session.commit()
			flash('New entry was successfully posted') 
	else:
		form = SetorForm(obj=setor)
		
		
	return render_template('editarSetor.html',form=form)
	
@setores.route('/remover/<int:id>',methods=('POST'))
def setorRemover(id):
	db.session.delete(obj)
	db.session.commit()
	return setoresListar()
	
