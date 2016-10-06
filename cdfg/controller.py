#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash, redirect, url_for
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField,HiddenField,SelectField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm

from DomainModel import db,CargoFuncaoGratificada,Salvar,Remover,ClasseCargoFuncao

cdfg = Blueprint('cdfg', __name__)

class CargoFuncaoGratificadaForm(ModelForm):
	class Meta:
		model = CargoFuncaoGratificada
		include = ['id']
	
@cdfg.route('/listar/')
def cdfgListar():
	cdfg = CargoFuncaoGratificada.query.all()
	return render_template('listarCdfg.html',listagem = cdfg, CL = ClasseCargoFuncao.__members__)
  
@cdfg.route('/editar/<int:id>',methods=('GET','POST'))
def cdfgEditar(id=0):
	
	if id == 0:
		cdfg = CargoFuncaoGratificada()
		cdfg.id = 0
	else:
		cdfg = CargoFuncaoGratificada.query.filter(CargoFuncaoGratificada.id == id).first()
	
	if request.method == 'POST':
		form = CargoFuncaoGratificadaForm(formdata=request.form)
		
		if form.validate():
			form.populate_obj(cdfg)
			if Salvar(cdfg):
				flash('Salvo com sucesso!','success')
			else: 
				flash('Falha ao salvar!','danger')
	else:
		form = CargoFuncaoGratificadaForm(obj=cdfg)		
		
	return render_template('editarCdfg.html',form=form)
	
@cdfg.route('/remover/<int:id>',methods=('GET','POST'))
def cdfgRemover(id):
	cdfg = CargoFuncaoGratificada.query.filter(CargoFuncaoGratificada.id == id).first()
	if Remover(cdfg):
		flash('Removido com sucesso!','success')
	else: 
		flash('Falha ao remover!','danger')
	return redirect(url_for('.cdfgListar'))
	
