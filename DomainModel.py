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

def Salvar(obj):
	try:
		db.session.add(obj)
		db.session.commit()
		return True
	except Exception as inst:
		print("ERRO SQLALCHEMY:")
		print(inst)
		db.session.rollback()
		return False
		
def Remover(obj):
	try:
		db.session.delete(obj)
		db.session.commit()
		return True
	except Exception as inst:
		print(inst)
		db.session.rollback()
		return False

class TipoServidor(enum.Enum):
	DE = "Docente Efetivo"
	DT = "Docente Temporário"
	TE = "Técnico-Administrativo Efetivo"
	TT = "Técnico-Administrativo Temporário"
	
class ClasseCargoFuncao(enum.Enum):
	FG = "Função Gratificada"
	CD = "Cargo de Direção"	
	
class SituacaoServidor(enum.Enum):
	A = "Ativo"
	P = "Pensionista"

class Titulacao(enum.Enum):
	EBA = "Ensino Básico e Fundamental"
	TEC = "Técnico"
	TLG = "Ensino Superior - Tecnologia"
	BAC = "Ensino Superior - Bacharelado"
	LIC = "Ensino Superior - Licenciatura"
	ESP = "Pós-Graduação Latu Sensu - Especialização/MBA"
	MES = "Pós-Graduação Strictu Sensu - Mestrado"
	DOC = "Pós-Graduação Strictu Sensu - Doutorado"


class TipoContaBancaria(enum.Enum):
	CC = "Conta Corrente"
	CP = "Conta Poupança"

class Sexo(enum.Enum):
	M = "Masculino"
	F = "Feminino"

class EstadoCivil(enum.Enum):
	S = "Solteiro"
	C = "Casado"

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

class Pessoa(db.Model):
	__tablename__ = 'pessoas'
	id = db.Column(db.Integer, primary_key = True)
	nome = db.Column(db.String(200), nullable=False)
	matricula = db.Column(db.String(12), unique=True)
	matriculaOrigem  = db.Column(db.String(12), unique=True)
	identificacaoUnica = db.Column(db.String(12), unique=True)
	tipoServidor = db.Column(db.String(2)) 
	situacaoServidor = db.Column(db.String(1))
	dataCadastroSiape = db.Column(db.DateTime)
	dataNascimento = db.Column(db.DateTime)
	estadoCivil  = db.Column(db.String(2))
	dataPrimeiroEmprego = db.Column(db.DateTime)
	dataPosse = db.Column(db.DateTime)
	dataExercicio = db.Column(db.DateTime)
	dataSaida = db.Column(db.DateTime)
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
	#enderecos = db.relationship("Endereco", backref="pessoa")
	endereco_id = db.Column(db.Integer, db.ForeignKey('enderecos.id'))
	endereco = db.relationship("Endereco")
	#telefones = db.relationship("Telefone", backref="pessoa")
	telefone1_id = db.Column(db.Integer, db.ForeignKey('telefones.id'))
	telefone1 = db.relationship("Telefone", foreign_keys=[telefone1_id])
	telefone2_id = db.Column(db.Integer, db.ForeignKey('telefones.id'))
	telefone2 = db.relationship("Telefone", foreign_keys=[telefone2_id])
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
	cargosfuncoesgratificadas = db.relationship("PessoaCargoFuncaoGratificada", backref="pessoa")
	titulos = db.relationship("Titulo", backref="pessoa")
	progressoes = db.relationship("Progressao", backref="pessoa")
	
	jornada = db.Column(db.String(2))
	
	campusLotacao_id  = db.Column(db.Integer, db.ForeignKey('campus.id'))
	campusLotacao = db.relationship("Campus", foreign_keys=[campusLotacao_id])
	campusExercicio_id  = db.Column(db.Integer, db.ForeignKey('campus.id'))
	campusExercicio = db.relationship("Campus", foreign_keys=[campusExercicio_id])
	
	cargo_id = db.Column(db.Integer, db.ForeignKey('cargos.id'))
	cargo = db.relationship("Cargo")
	
		
	def __repr__(self):
		return '<Pessoa %r>' % self.nome
				
class ClasseNivel(db.Model):
	__tablename__ = 'classesniveis'
	id = db.Column(db.Integer, primary_key = True)
	tipoServidor = db.Column(db.String(2))
	classe = db.Column(db.String(10))
	nivel = db.Column(db.String(5))
	
	def __repr__(self):
		return '<Classe/Nivel %r>' % self.classe

class Progressao(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	classenivel_id = db.Column(db.Integer, db.ForeignKey('classesniveis.id'))
	classenivel = db.relationship('ClasseNivel')
	dataInicio = db.Column(db.DateTime)
	dataTermino = db.Column(db.DateTime)
	
	pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))
	
	
class Endereco(db.Model):
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
	
	
class Telefone(db.Model):
	__tablename__ = 'telefones'
	id = db.Column(db.Integer, primary_key = True)
	ddd = db.Column(db.String(2))
	numero = db.Column(db.String(12))
	ramal = db.Column(db.String(8))	
	
	#pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))

class Cargo(db.Model):	
	__tablename__ = 'cargos'
	id = db.Column(db.Integer, primary_key = True)
	tipoServidor = db.Column(db.String(2))
	nome = db.Column(db.String(200))
	

class CargoFuncaoGratificada(db.Model):	
	__tablename__ = 'cargosfuncoesgratificadas'
	id = db.Column(db.Integer, primary_key = True)
	classe   = db.Column(db.String(2)) #ClasseCargoFuncao
	nivel    = db.Column(db.String(5)) 
	
class PessoaCargoFuncaoGratificada(db.Model):
	__tablename__ = 'pessoascargosfuncoesgratificadas'
	id = db.Column(db.Integer, primary_key = True)
	dataInicio = db.Column(db.DateTime)
	dataTermino = db.Column(db.DateTime)
	descricao = db.Column(db.String(120))
		
	pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))
	cargofuncaogratificada_id = db.Column(db.Integer, db.ForeignKey('cargosfuncoesgratificadas.id'))
	cargofuncaogratificada = db.relationship("CargoFuncaoGratificada")
	
	
class Campus(db.Model):
	__tablename__ = 'campus'
	id = db.Column(db.Integer, primary_key = True)
	sigla = db.Column(db.String(120), unique=True,info={'label': 'Sigla'})
	nome = db.Column(db.String(120), unique=True,info={'label': 'Nome'})
		

class Setor(db.Model):
	__tablename__ = 'setores'
	id = db.Column(db.Integer, primary_key = True)
	sigla = db.Column(db.String(120), unique=True,info={'label': 'Sigla'})
	nome = db.Column(db.String(120), unique=True,info={'label': 'Nome'})
	telefone = db.Column(db.String(12),info={'label': 'Telefone'})
	
	campus_id = db.Column(db.Integer, db.ForeignKey('campus.id'),info={'label': 'Campus'})
	campus = db.relationship('Campus')
	
	def __repr__(self):
		return '<Setor %r>' % self.nome

		
class Titulo(db.Model):
	__tablename__ = 'titulos'
	id = db.Column(db.Integer, primary_key = True)
	titulo = db.Column(db.String(3))
	area = db.Column(db.String(120)) 
	instituicao = db.Column(db.String(120))
	dataInicio = db.Column(db.DateTime)
	dataTermino = db.Column(db.DateTime)
	
	pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))

	def __repr__(self):
		return '<Titulo %r>' % self.titulo

