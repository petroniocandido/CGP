#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField,HiddenField,SelectField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from DomainModel import db,Cargo,Salvar,Remover,TipoServidor

cargos = Blueprint('cargos', __name__)

class CargoForm(ModelForm):
	class Meta:
		model = Cargo
		include = ['id']
	
	tipoServidor = SelectField('Tipo de Servidor', choices=[(c.name, c.value) for c in TipoServidor])
	
@cargos.route('/listar/')
def cargosListar():
	cargos = Cargo.query.all()
	return render_template('listarCargos.html',listagem = cargos, TS = TipoServidor.__members__)
  
@cargos.route('/editar/<int:id>',methods=('GET','POST'))
def CargoEditar(id=0):
	
	if id == 0:
		cargos = Cargo()
		cargos.id = 0
	else:
		cargos = Cargo.query.filter(Cargo.id == id).first()
	
	if request.method == 'POST':
		form = CargoForm(formdata=request.form)
		
		if form.validate():
			form.populate_obj(cargos)
			if Salvar(cargos):
				flash('Salvo com sucesso!','success')
			else: 
				flash('Falha ao salvar!','danger')
	else:
		form = CargoForm(obj=cargos)
		
		
	return render_template('editarCargo.html',form=form)
	
@cargos.route('/remover/<int:id>',methods=('GET','POST'))
def CargoRemover(id):
	cargos = Cargo.query.filter(Cargo.id == id).first()
	if Remover(cargos):
		flash('Removido com sucesso!','success')
	else: 
		flash('Falha ao remover!','danger')
	cargos = Cargo.query.all()
	return render_template('listarCargos.html',listagem = cargos, TS = TipoServidor.__members__)
	
