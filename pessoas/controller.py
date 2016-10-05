#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash
from flask import Blueprint
from flask_wtf import Form
from wtforms_alchemy import ModelForm, ModelFormField, ModelFieldList
from wtforms import StringField,HiddenField,SelectField,FormField,BooleanField,FieldList
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired,Length,Optional

from DomainModel import db,Pessoa,Salvar,Remover,EstadoCivil,TipoServidor,SituacaoServidor,\
UF,JornadaTrabalho,Sexo,TipoSanguineo,TipoContaBancaria,Telefone,Endereco,Cargo,Titulo,Titulacao

pessoas = Blueprint('pessoas', __name__)

class TelefoneForm(ModelForm):
	class Meta:
		model = Telefone

class EnderecoForm(ModelForm):
	class Meta:
		model = Endereco
	estado = SelectField('UF', choices=[(c.value, c.name) for c in UF])
	
	
class PessoaForm(ModelForm):
	class Meta:
		model = Pessoa
		include = ['id']
	tipoServidor = SelectField('Tipo de Servidor', choices=[(c.name, c.value) for c in TipoServidor])
	jornada = SelectField('Regime/Jornada', choices=[(c.name,c.value) for c in JornadaTrabalho])
	situacaoServidor = SelectField('Situação do Servidor', choices=[(c.name, c.value) for c in SituacaoServidor])
	ufNascimento  = SelectField('UF Nascimento', choices=[(c.value, c.name) for c in UF])
	tipoSanguineo = SelectField('Tipo Sanguineo', choices=[(c.name,c.value) for c in TipoSanguineo])
	sexo  = SelectField('Sexo', choices=[(c.name, c.value) for c in Sexo])
	rg_UF = SelectField('UF', choices=[(c.name,c.value) for c in UF])
	tituloEleitor_UF = SelectField('UF', choices=[(c.name,c.value) for c in UF])
	pagamento_TipoConta = SelectField('Tipo Conta', choices=[(c.name,c.value) for c in TipoContaBancaria])
	telefone1 = ModelFormField(TelefoneForm) #, "Telefone 1", default=lambda: Telefone())
	telefone2 = ModelFormField(TelefoneForm) #, "Telefone 2", default=lambda: Telefone())
	endereco = ModelFormField(EnderecoForm) #, "Endereço", default=lambda: Endereco())
	cargo_id = SelectField('Cargo', coerce=int, choices=[(c.id, c.nome) for c in Cargo.query.order_by('nome')])
	
	
@pessoas.route('/listar/')
def pessoasListar():
	pessoas = Pessoa.query.all()
	return render_template('listarPessoas.html',listagem = pessoas, TS = TipoServidor.__members__)

@pessoas.route('/editar/<int:id>',methods=('GET','POST'))
def pessoaEditar(id=0):
	
	if id == 0:
		pessoa = Pessoa()
		pessoa.id = 0
		print(id)
	else:
		pessoa = Pessoa.query.filter(Pessoa.id == id).first()
	
	if request.method == 'POST':
		form = PessoaForm(formdata=request.form)
		
		if form.validate():
			form.populate_obj(pessoa)
			if Salvar(pessoa):
				flash('Salvo com sucesso!','success')
			else: 
				flash('Falha ao salvar!','danger')
		else:
			print("ERRO!!!")
			print(form.errors)
	else:
		form = PessoaForm(obj=pessoa)
		
	return render_template('editarPessoa.html',form=form, titulos=pessoa.titulos, TIT = Titulacao.__members__)
	
@pessoas.route('/remover/<int:id>',methods=('GET','POST'))
def pessoaRemover(id):
	pessoa = Pessoa.query.filter(Pessoa.id == id).first()
	if Remover(pessoa):
		flash('Removido com sucesso!','success')
	else: 
		flash('Falha ao remover!','danger')
	pessoas = Pessoa.query.all()
	return render_template('listarPessoas.html',listagem = pessoas, TS = TipoServidor.__members__)
	
