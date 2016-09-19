#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declared_attr
import enum

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/CGP'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class TipoServidor(enum.Enum):
	TAE = "Técnico-Administrativo"
	DOC = "Docente"
	
class SituacaoServidor(enum.Enum):
	Ativo = "1"
	Pensionista = "2"

class Titulacao(enum.Enum):
	EnsinoBasico = "Ensino Básico e Fundamental"
	Tecnico = "Técnico"
	Tecnologo = "Ensino Superior - Tecnologia"
	Bacharel = "Ensino Superior - Bacharelado"
	Licenciado = "Ensino Superior - Licenciatura"
	Especialista = "Pós-Graduação Latu Sensu - Especialização/MBA"
	Mestre = "Pós-Graduação Strictu Sensu - Mestrado"
	Doutor = "Pós-Graduação Strictu Sensu - Doutorado"


class TipoContaBancaria(enum.Enum):
	ContaCorrente = "Conta Corrente"
	ContaPoupanca = "Conta Poupança"

class Sexo(enum.Enum):
	M = "Masculino"
	F = "Fminino"

class EstadoCivil(enum.Enum):
	Solteiro = "Solteiro(a)"
	Casado = "Casado(a)"

class TipoSanguineo(enum.Enum):
	an = "A-"
	ap = "A+"
	bn = "B-"
	bp = "B+"
	abn = "AB-"
	abp = "AB+"
	on = "O-"
	op = "O+"

class JornadaTrabalho(enum.Enum):
	vh = "20"
	qh = "40"
	de = "DE"

class UF(enum.Enum):
	AC = "AC"
	AL = "AL"
	AM = "AM"
	AP = "AP"
	BA = "BA"
	CE = "CE"
	DF = "DF"
	ES = "ES"
	GO = "GO"
	MA = "MA"
	MS = "MS"
	MG = "MG"
	MT = "MT"
	PA = "PA"
	PB = "PB"
	PE = "PE"
	PI = "PI"
	PR = "PR"
	RJ = "RJ"
	RN = "RN"
	RS = "RS"
	RO = "RO"
	RR = "RR"
	SC = "SC"
	SE = "SE"
	SP = "SP"
	TO = "TO"
	
# Define a base model for other database tables to inherit
class Entidade(db.Model):
	
	__abstract__  = True
	id = db.Column(db.Integer, primary_key=True)
	dataCriacao  = db.Column(db.DateTime, default=db.func.current_timestamp(),nullable=False)
	dataUltimaModificacao = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(),nullable=False)
	
	#@declared_attr
	#def usuarioCriacao_id(cls): 
	#	return db.Column(db.Integer, db.ForeignKey('pessoas.id'))
	
	#@declared_attr
	#def usuarioCriacao(cls): 
	#	return db.relationship('Pessoa', foreign_keys=[usuarioCriacao_id])
		
	#@declared_attr
	#def usuarioUltimaModificacao_id(cls): 
	#	return db.Column(db.Integer, db.ForeignKey('pessoas.id'))
		
	#@declared_attr
	#def usuarioUltimaModificacao(cls): 
	#	return db.relationship('Pessoa', foreign_keys=[usuarioUltimaModificacao_id])

class Pessoa(Entidade):
	__tablename__ = 'pessoas'
	#id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(200), nullable=False)
	matricula = db.Column(db.String(12), unique=True)
	matriculaOrigem  = db.Column(db.String(12), unique=True)
	identificacaoUnica = db.Column(db.String(12), unique=True)
	tipoServidor = db.Column(db.String(2))
	situacaoServidor = db.Column(db.String(1))
	dataCadastroSiape = db.Column(db.DateTime)
	dataNascimento = db.Column(db.DateTime)
	estadoCivil  = db.Column(db.String(10))
	dataPrimeiroEmprego = db.Column(db.DateTime)
	nacionalidade = db.Column(db.String(200))
	ufNascimento  = db.Column(db.String(2))
	nomeMae = db.Column(db.String(200))
	nomePai = db.Column(db.String(200))
	naturalidade = db.Column(db.String(200))
	tipoSanguineo = db.Column(db.String(3))
	sexo  = db.Column(db.String(1))
	possuiDeficiencia = db.Column(db.Boolean)
	TipoDeficiencia = db.Column(db.String(200))
	raca_cor = db.Column(db.String(200))
	enderecos = db.relationship("Endereco", backref="pessoa")
	telefones = db.relationship("Telefone", backref="pessoa")
	email_Pessoal = db.Column(db.String(120), unique=True)
	email_Institucional = db.Column(db.String(120), unique=True)
	curriculumLattes = db.Column(db.String(120), unique=True)
	rg_Numero = db.Column(db.String(200))
	rg_OrgaoExpedidor = db.Column(db.String(200))
	rg_UF = db.Column(db.String(2))
	rg_Emissao = db.Column(db.DateTime)
	cpf = db.Column(db.String(200), unique=True)
	pis_pasep = db.Column(db.String(20))
	tituloEleitor = db.Column(db.String(20))
	tituloEleitor_UF = db.Column(db.String(2))
	tituloEleitor_Zona = db.Column(db.String(5))
	tituloEleitor_Secao = db.Column(db.String(5))
	tituloEleitor_Emissao = db.Column(db.DateTime)
	certificadoMilitar = db.Column(db.String(20))
	certificadoMilitar_Orgao = db.Column(db.String(200))
	certificadoMilitar_Serie = db.Column(db.String(20))
	passaporte = db.Column(db.String(20))
	pagamento_Banco = db.Column(db.String(5))
	pagamento_Agencia = db.Column(db.String(12))
	pagamento_Conta = db.Column(db.String(12))
	pagamento_TipoConta = db.Column(db.String(2))
	cargos = db.relationship("Cargo", backref="pessoa")
	funcoes = db.relationship("Funcao", backref="pessoa")
	titulos = db.relationship("Titulo", backref="pessoa")
	progressoes = db.relationship("Progressao", backref="pessoa")
	
	jornada = db.Column(db.String(2))
	
		
	def __repr__(self):
		return '<Pessoa %r>' % self.nome
			
class ClasseNivel(Entidade):
	__tablename__ = 'classesniveis'
	id = db.Column(db.Integer, primary_key = True)
	classe = db.Column(db.String(5))
	nivel = db.Column(db.Integer)
	
	def __init__(self,classe,nivel):
		self.classe = classe
		self.nivel = nivel
	
	def __repr__(self):
		return '<Classe/Nivel %r>' % self.classe

class Progressao(Entidade):
	id = db.Column(db.Integer, primary_key = True)
	classenivel_id = db.Column(db.Integer, db.ForeignKey('classesniveis.id'))
	classenivel = db.relationship('ClasseNivel')
	dataInicio = db.Column(db.DateTime)
	dataTermino = db.Column(db.DateTime)
	
	pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))
	#pessoa = db.relationship('Pessoa',  backref=db.backref('progressoes_fk', lazy='dynamic'))

	def __init__(self,classenivel,dataInicio,dataTermino,pessoa):
		self.classenivel = classenivel
		self.dataInicio = dataInicio
		self.dataTermino = dataTermino
		self.pessoa = pessoa
	
	
class Endereco(Entidade):
	__tablename__ = 'enderecos'
	id = db.Column(db.Integer, primary_key = True)
	logradouro  = db.Column(db.String(200))
	numero  = db.Column(db.String(10))
	complemento  = db.Column(db.String(200))
	bairro  = db.Column(db.String(200))
	municipio  = db.Column(db.String(200))
	pais  = db.Column(db.String(100))
	estado = db.Column(db.String(2))
	cep = db.Column(db.String(10))
	
	pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))
	#pessoa = db.relationship('Pessoa',  backref='enderecos_fk')
	
	def __init__(self,logradouro, numero, complemento, bairro, municipio, pais, estado, cep, pessoa):
		self.logradouro = logradouro
		self.numero = numero
		self.complemento = complemento
		self.bairro = bairro
		self.municipio = municipio
		self.pais = pais
		self.estado = estado
		self.cep = cep
		self.pessoa = pessoa
	
class Telefone(Entidade):
	__tablename__ = 'telefones'
	id = db.Column(db.Integer, primary_key = True)
	ddd = db.Column(db.String(2))
	numero = db.Column(db.String(12))
	ramal = db.Column(db.String(8))
	fixo = db.Column(db.Boolean)
	celular = db.Column(db.Boolean)
	prestadora = db.Column(db.String(12))
	
	pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))
	#pessoa = db.relationship('Pessoa',  backref=db.backref('telefones_fk', lazy='dynamic'))
	
	def __init__(self, ddd, numero, ramal, fixo, celular, prestadora):
		self.ddd = ddd
		self.numero = numero
		self.ramal = ramal
		self.fixo = fixo
		self.celular = celular
		self.prestadora = prestadora

	
class Cargo(Entidade):
	__tablename__ = 'cargos'
	id = db.Column(db.Integer, primary_key = True)
	cargo  = db.Column(db.String(200))
	classe   = db.Column(db.String(200))
	padrao   = db.Column(db.String(200))
	dataPosse = db.Column(db.DateTime)
	dataSaida = db.Column(db.DateTime)
	codigoVaga  = db.Column(db.String(200))
	ingresso = db.Column(db.DateTime)
	exercicio = db.Column(db.DateTime)
	
	pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))
	#pessoa = db.relationship('Pessoa',  backref=db.backref('cargos_fk', lazy='dynamic'))
	
	
class Funcao(Entidade):
	__tablename__ = 'funcoes'
	id = db.Column(db.Integer, primary_key = True)
	sigla = db.Column(db.String(120), unique=True)
	codigo = db.Column(db.String(120), unique=True)
	nome = db.Column(db.String(120), unique=True)
	dataIngresso = db.Column(db.DateTime)
	dataSaida = db.Column(db.DateTime)
	atividade = db.Column(db.String(120), unique=True)
	
	pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))
	#pessoa = db.relationship('Pessoa',  backref=db.backref('funcoes_fk', lazy='dynamic'))
	
	def __init__(self, sigla, codigo, nome, dataIngresso, dataSaida, atividade):
		self.sigla = sigla
		self.codigo = codigo
		self.nome = nome
		self.dataIngresso = dataIngresso
		self.dataSaida = dataSaida
		self.atividade = atividade

	
class Campus(Entidade):
	__tablename__ = 'campus'
	id = db.Column(db.Integer, primary_key = True)
	sigla = db.Column(db.String(120), unique=True)
	nome = db.Column(db.String(120), unique=True)
	
	def __init__(self, sigla, nome):
		self.sigla = sigla
		self.nome = nome


class Setor(Entidade):
	__tablename__ = 'setores'
	id = db.Column(db.Integer, primary_key = True)
	sigla = db.Column(db.String(120), unique=True)
	nome = db.Column(db.String(120), unique=True)
	telefone = db.Column(db.String(12))
	
	campus_id = db.Column(db.Integer, db.ForeignKey('campus.id'))
	campus = db.relationship('Campus')
	
	def __init__(self, sigla, nome):
		self.sigla = sigla
		self.nome = nome

	def __repr__(self):
		return '<Setor %r>' % self.nome

		
class Titulo(Entidade):
	__tablename__ = 'titulos'
	id = db.Column(db.Integer, primary_key = True)
	titulo = db.Column(db.String(20))
	area = db.Column(db.String(120)) 
	instituicao = db.Column(db.String(120))
	dataInicio = db.Column(db.DateTime)
	dataTermino = db.Column(db.DateTime)
	
	pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))
	#pessoa = db.relationship('Pessoa',  backref=db.backref('titulos_fk', lazy='dynamic'))
	
	def __init__(self, titulo, area, instituicao, dataInicio, dataTermino, pessoa):
		self.titulo = titulo
		self.area = area
		self.instituicao = instituicao
		self.dataInicio = dataInicio
		self.dataTermino = dataTermino
		self.pessoa = pessoa

	def __repr__(self):
		return '<Titulo %r>' % self.titulo

