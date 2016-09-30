#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField,HiddenField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from DomainModel import db,Campus,Salvar,Remover

campus = Blueprint('campus', __name__)

class CampusForm(ModelForm):
	class Meta:
		model = Campus
		include = ['id']
	
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
			if Salvar(campus):
				flash('Salvo com sucesso!','success')
			else: 
				flash('Falha ao salvar!','danger')
	else:
		form = CampusForm(obj=campus)
		
		
	return render_template('editarCampus.html',form=form)
	
@campus.route('/remover/<int:id>',methods=('GET','POST'))
def CampusRemover(id):
	campus = Campus.query.filter(Campus.id == id).first()
	if Remover(campus):
		flash('Removido com sucesso!','success')
	else: 
		flash('Falha ao remover!','danger')
	campi = Campus.query.all()
	return render_template('listarCampus.html',listagem = campi)
	
