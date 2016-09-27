#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField,HiddenField,SelectField,FormField,BooleanField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired,Length,Optional

from DomainModel import db,Pessoa,Salvar,Remover,EstadoCivil,TipoServidor,SituacaoServidor,UF,JornadaTrabalho,Sexo,TipoSanguineo,TipoContaBancaria

pessoas = Blueprint('pessoas', __name__)

#class CertificadoMilitarForm(Form):
	
class PessoaForm(Form):
	id = HiddenField('id')
	nome = StringField('Nome', validators=[DataRequired(),Length(max=200)])
	#matriculaOrigem  = db.Column(db.String(12), unique=True)
	#identificacaoUnica = db.Column(db.String(12), unique=True)
	
	#siape = FormField(SiapeForm,"SIAPE")
	matricula = StringField('Nº SIAPE', validators=[DataRequired()])
	dataCadastroSiape = DateField("Data Cadastro SIAPE", format="f%Y-%m-%d", validators=[Optional()])
	
	#servidor = FormField(ServidorForm,"Tipo/Regime")
	tipoServidor = SelectField('Tipo de Servidor', choices=[(c.name, c.value) for c in TipoServidor])
	jornada = SelectField('Regime/Jornada', choices=[(c.name,c.value) for c in JornadaTrabalho])
	situacaoServidor = SelectField('Situação do Servidor', choices=[(c.name, c.value) for c in SituacaoServidor])
	
	dataNascimento = DateField("Data Nascimento", format="%Y-%m-%d", validators=[Optional()])
	estadoCivil  = SelectField('Estado Civil', choices=[(c.name,c.value) for c in EstadoCivil])
	dataPrimeiroEmprego = DateField("Data Primeiro Emprego", format="f%Y-%m-%d", validators=[Optional()])
	nacionalidade = StringField('Nacionalidade')
	ufNascimento  = SelectField('UF Nascimento', choices=[(c.value, c.name) for c in UF])
	nomeMae = StringField('Nome Mae')
	nomePai = StringField('Nome Pai')
	naturalidade = StringField('Naturalidade')
	tipoSanguineo = SelectField('Tipo Sanguineo', choices=[(c.name,c.value) for c in TipoSanguineo])
	sexo  = SelectField('Sexo', choices=[(c.name, c.value) for c in Sexo])
	possuiDeficiencia = BooleanField('Possui Deficiência')
	TipoDeficiencia = StringField('Tipo Deficiência')
	raca_cor = StringField('Raça/Cor')
	email_Pessoal = StringField('E-mail Pessoal')
	email_Institucional = StringField('E-mail Institucional')
	curriculumLattes = StringField('Curriculum Lattes')
	#rg = FormField(RGForm,"Identidade")
	rg_Numero = StringField('Nº')
	rg_OrgaoExpedidor = StringField('Org. Exp.')
	rg_UF = SelectField('UF', choices=[(c.name,c.value) for c in UF])
	rg_Emissao = DateField("Emissão", format="f%Y-%m-%d", validators=[Optional()])
	
	cpf = StringField('CPF')
	pis_pasep = StringField('PIS/PASEP')
	#tituloEleitor = FormField(TituloEleitorForm,"Título de Eleitor")
	tituloEleitor = StringField('Nº')
	tituloEleitor_UF = SelectField('UF', choices=[(c.name,c.value) for c in UF])
	tituloEleitor_Zona = StringField('Zona')
	tituloEleitor_Secao = StringField('Seção')
	tituloEleitor_Emissao = DateField("Emissão", format="f%Y-%m-%d", validators=[Optional()])
	
	#certificadoMilitar = FormField(CertificadoMilitarForm,"Certificado de Militar")
	certificadoMilitar = StringField('Nº ')
	certificadoMilitar_Orgao = StringField('Orgão')
	certificadoMilitar_Serie = StringField('Série')
	
	passaporte = StringField('Passaporte')
	#pagamento = FormField(PagamentoForm,"Conta Pagamento")
	pagamento_Banco = StringField('Banco')
	pagamento_Agencia = StringField('Agência')
	pagamento_Conta = StringField('Conta Corrente')
	pagamento_TipoConta = SelectField('Tipo Conta', choices=[(c.name,c.value) for c in TipoContaBancaria])
	
	
@pessoas.route('/listar/')
def setoresListar():
	pessoas = Pessoa.query.all()
	return render_template('listarPessoas.html',listagem = pessoas, TS = TipoServidor.__members__)
  
@pessoas.route('/editar/<int:id>',methods=('GET','POST'))
def setorEditar(id=0):
	
	if id == 0:
		pessoa = Pessoa()
		pessoa.id = 0
		print(id)
	else:
		pessoa = Pessoa.query.filter(Pessoa.id == id).first()
	
	if request.method == 'POST':
		form = PessoaForm(formdata=request.form)
		
		if form.validate():
			print("validou")
			form.populate_obj(pessoa)
			if Salvar(pessoa):
				flash('Salvo com sucesso!','success')
			else: 
				flash('Falha ao salvar!','danger')
		else:
			print(form.errors)
	else:
		form = PessoaForm(obj=pessoa)
		
	return render_template('editarPessoa.html',form=form)
	
@pessoas.route('/remover/<int:id>',methods=('GET','POST'))
def setorRemover(id):
	pessoa = Pessoa.query.filter(Pessoa.id == id).first()
	if Remover(pessoa):
		flash('Removido com sucesso!','success')
	else: 
		flash('Falha ao remover!','danger')
	pessoas = Pessoa.query.all()
	return render_template('listarPessoas.html',listagem = pessoas, TS = TipoServidor.__members__)
	
