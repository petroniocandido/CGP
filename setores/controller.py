from flask import Flask, render_template, request
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

from DomainModel import db,Setor

setores = Blueprint('setores', __name__)

class SetorForm(Form):
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
		setor = Setor("","")
	else:
		setor = Setor.get(id)
	
	if request.method == 'POST':
		form = SetorForm(formdata=request.form)
		
		setor.sigla = form.sigla.data
		setor.nome = form.nome.data
		setor.telefone = form.telefone.data
		
		db.session.add(setor)
		
	else:
		form = SetorForm(obj=setor)
		
		
	return render_template('editarSetor.html',form=form)

@setores.route('/remover/<int:id>',methods=('POST'))
def setorRemover(id):
	return setoresListar()
	
