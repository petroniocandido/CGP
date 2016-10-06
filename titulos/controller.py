#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash, redirect, url_for
from flask import Blueprint
from flask_wtf import Form
from wtforms_alchemy import ModelForm, ModelFormField, ModelFieldList
from wtforms import StringField,HiddenField,SelectField,FormField,BooleanField,FieldList
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired,Length,Optional

from DomainModel import db,Pessoa,Salvar,Remover,Titulo

titulos = Blueprint('titulos', __name__)

class TituloForm(ModelForm):
	class Meta:
		model = Titulo
		include = ['id','pessoa_id']
	
@titulos.route('/editar/<int:pessoa_id>,<int:titulo_id>',methods=('GET','POST'))
def tituloEditar(pessoa_id=0,titulo_id=0):
	if titulo_id == 0:
		titulo = Titulo()
		titulo.id = 0
		titulo.pessoa_id = pessoa_id
	else:
		titulo = Titulo.query.filter(Titulo.id == titulo_id).first()
		
	if request.method == 'POST':
		form = TituloForm(formdata=request.form)
		
		if form.validate():
			form.populate_obj(titulo)
			if Salvar(titulo):
				flash('Salvo com sucesso!','success')
			else: 
				flash('Falha ao salvar!','danger')
		else:
			print("ERRO!!!")
			print(form.errors)
	else:
		form = TituloForm(obj=titulo)
		
	return render_template('editarTitulo.html',form=form)

@titulos.route('/remover/<int:id>',methods=('GET','POST'))
def tituloRemover(id):
	titulo = Titulo.query.filter(Titulo.id == id).first()
	pessoa_id = titulo.pessoa_id
	if Remover(titulo):
		flash('Removido com sucesso!','success')
	else: 
		flash('Falha ao remover!','danger')
	return redirect(url_for('pessoas.pessoaEditar',id=pessoa_id))
	
