#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField,HiddenField,SelectField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from DomainModel import db,Setor,Campus,Salvar,Remover

setores = Blueprint('setores', __name__)

class SetorForm(ModelForm):
	class Meta:
		model = Setor
		include = ['id']
	
	campus_id = SelectField('Campus', coerce=int, choices=[(c.id, c.sigla) for c in Campus.query.order_by('sigla')])
	
@setores.route('/listar/')
def setoresListar():
	setores = Setor.query.all()
	return render_template('listarSetores.html',listagem = setores)
  
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
			if Salvar(setor):
				flash('Salvo com sucesso!','success')
			else: 
				flash('Falha ao salvar!','danger')
	else:
		form = SetorForm(obj=setor)
		
	return render_template('editarSetor.html',form=form)
	
@setores.route('/remover/<int:id>',methods=('GET','POST'))
def setorRemover(id):
	setor = Setor.query.filter(Setor.id == id).first()
	if Remover(setor):
		flash('Removido com sucesso!','success')
	else: 
		flash('Falha ao remover!','danger')
	setores = Setor.query.all()
	return render_template('listarSetores.html',listagem = setores)
	
