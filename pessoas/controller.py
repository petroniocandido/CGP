#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask, render_template, request, flash
from flask import Blueprint
from flask_wtf import Form
from wtforms import StringField,HiddenField,SelectField,DateField,FormField,BooleanField
from wtforms.validators import DataRequired

from DomainModel import db,Pessoa,Salvar,Remover,EstadoCivil,TipoServidor,SituacaoServidor,UF,JornadaTrabalho,Sexo,TipoSanguineo

pessoas = Blueprint('pessoas', __name__)

class CertificadoMilitarForm(Form):
	certificadoMilitar = StringField('Nº ')
	certificadoMilitar_Orgao = StringField('Orgão')
	certificadoMilitar_Serie = StringField('Série')

class PagamentoForm(Form):
	pagamento_Banco = StringField('Banco')
	pagamento_Agencia = StringField('Agência')
	pagamento_Conta = StringField('Conta Corrente')
	pagamento_TipoConta = SelectField('Tipo Conta', choices=[(c.name,c.value) for c in UF])
	
class TituloEleitorForm(Form):
	tituloEleitor = StringField('Nº')
	tituloEleitor_UF = SelectField('UF', choices=[(c.name,c.value) for c in UF])
	tituloEleitor_Zona = StringField('Zona')
	tituloEleitor_Secao = StringField('Seção')
	tituloEleitor_Emissao = DateField("Emissão", format="%d/%m/%y")
	
class RGForm(Form):
	rg_Numero = StringField('Nº')
	rg_OrgaoExpedidor = StringField('Org. Exp.')
	rg_UF = SelectField('UF', choices=[(c.name,c.value) for c in UF])
	rg_Emissao = DateField("Emissão", format="%d/%m/%y")

class PessoaForm(Form):
	id = HiddenField('id')
	nome = StringField('Pessoa', validators=[DataRequired()])
	matricula = StringField('SIAPE', validators=[DataRequired()])
	#matriculaOrigem  = db.Column(db.String(12), unique=True)
	#identificacaoUnica = db.Column(db.String(12), unique=True)
	tipoServidor = SelectField('Tipo de Servidor', choices=[(c.name, c.value) for c in TipoServidor])
	situacaoServidor = SelectField('Situação do Servidor', choices=[(c.value, c.name) for c in SituacaoServidor])
	dataCadastroSiape = DateField("Data Cadastro Siape", format="%d/%m/%y")
	dataNascimento = DateField("Data Nascimento", format="%d/%m/%y")
	estadoCivil  = SelectField('Estado Civil', choices=[(c.name,c.value) for c in EstadoCivil])
	dataPrimeiroEmprego = DateField("Data Primeiro Emprego", format="%d/%m/%y")
	nacionalidade = StringField('Nacionalidade')
	ufNascimento  = SelectField('UF Nascimento', choices=[(c.value, c.name) for c in UF])
	nomeMae = StringField('Nome Mae')
	nomePai = StringField('Nome Pai')
	naturalidade = StringField('Naturalidade')
	tipoSanguineo = SelectField('Tipo Sanguineo', choices=[(c.name,c.value) for c in TipoSanguineo])
	sexo  = SelectField('Sexo', choices=[(c.value, c.name) for c in Sexo])
	possuiDeficiencia = BooleanField('Possui Deficiência')
	TipoDeficiencia = StringField('Tipo Deficiência')
	raca_cor = StringField('Raça/Cor')
	email_Pessoal = StringField('E-mail Pessoal')
	email_Institucional = StringField('E-mail Institucional')
	curriculumLattes = StringField('Curriculum Lattes')
	rg = FormField(RGForm,"Identidade")
	cpf = StringField('CPF')
	pis_pasep = StringField('PIS/PASEP')
	tituloEleitor = FormField(TituloEleitorForm,"Título de Eleitor")
	certificadoMilitar = FormField(CertificadoMilitarForm,"Certificado de Militar")
	passaporte = StringField('Passaporte')
	pagamento = FormField(PagamentoForm,"Conta Pagamento")
	jornada = SelectField('Regime/Jornada', choices=[(c.name,c.value) for c in JornadaTrabalho])
	
@pessoas.route('/listar/')
def setoresListar():
	pessoas = Pessoa.query.all()
	return render_template('listarPessoas.html',listagem = pessoas, TS = TipoServidor.__members__)
  
@pessoas.route('/editar/<int:id>',methods=('GET','POST'))
def setorEditar(id=0):
	
	if id == 0:
		pessoa = Pessoa()
		pessoa.id = 0
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
	
