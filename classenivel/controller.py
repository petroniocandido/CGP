#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField,HiddenField,SelectField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from DomainModel import db,ClasseNivel,TipoServidor,Salvar,Remover

classenivel = Blueprint('classenivel', __name__)

class ClasseNivelForm(ModelForm):
	class Meta:
		model = ClasseNivel
		include = ['id']
	tipoServidor = SelectField('Tipo de Servidor', choices=[(c.name, c.value) for c in TipoServidor])
	
@classenivel.route('/listar/')
def campusListar():
	classes = ClasseNivel.query.all()
	return render_template('listarClasseNivel.html',listagem = classes, TS = TipoServidor.__members__)
  
@classenivel.route('/editar/<int:id>',methods=('GET','POST'))
def CampusEditar(id=0):
	
	if id == 0:
		classenivel = ClasseNivel()
		classenivel.id = 0
	else:
		classenivel = ClasseNivel.query.filter(ClasseNivel.id == id).first()
	
	if request.method == 'POST':
		form = ClasseNivelForm(formdata=request.form)
		
		if form.validate():
			form.populate_obj(classenivel)
			if Salvar(classenivel):
				flash('Salvo com sucesso!','success')
			else: 
				flash('Falha ao salvar!','danger')
	else:
		form = ClasseNivelForm(obj=classenivel)
		
		
	return render_template('editarClasseNivel.html',form=form)
	
@classenivel.route('/remover/<int:id>',methods=('GET','POST'))
def CampusRemover(id):
	classenivel = ClasseNivel.query.filter(ClasseNivel.id == id).first()
	if Remover(classenivel):
		flash('Removido com sucesso!','success')
	else: 
		flash('Falha ao remover!','danger')
	classes = ClasseNivel.query.all()
	return render_template('listarClasseNivel.html',listagem = classes)
	
