#!/usr/bin/python
# -*- coding: utf8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declared_attr
import enum
from wtforms.fields.html5 import DateField

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
	nome = db.Column(db.String(200), nullable=False,info={'label': 'Nome'})
	matricula = db.Column(db.String(12), unique=True,info={'label': 'Matrícula'})
	matriculaOrigem  = db.Column(db.String(12), unique=True,info={'label': 'Matrícula de Origem'})
	identificacaoUnica = db.Column(db.String(12), unique=True,info={'label': 'Identificação Única'})
	tipoServidor = db.Column(db.String(2),info={'label': 'Tipo Servidor', 'choices': [(c.name, c.value) for c in TipoServidor]}) 
	situacaoServidor = db.Column(db.String(1),info={'label': 'Situação do Servidor', 'choices': [(c.name, c.value) for c in SituacaoServidor]})
	dataCadastroSiape = db.Column(db.DateTime,info={'label': 'Data de Cadastro SIAPE'})
	dataNascimento = db.Column(db.DateTime,info={'label': 'Data Nascimento','form_field_class': DateField})
	estadoCivil  = db.Column(db.String(2),info={'label': 'Estado Civil', 'choices': [(c.name, c.value) for c in EstadoCivil]})
	dataPrimeiroEmprego = db.Column(db.DateTime,info={'label': 'Data do Primeiro Emprego'})
	dataPosse = db.Column(db.DateTime,info={'label': 'Data Posse','form_field_class': DateField})
	dataExercicio = db.Column(db.DateTime,info={'label': 'Data Exercício','form_field_class': DateField})
	dataSaida = db.Column(db.DateTime,info={'label': 'Data Saída','form_field_class': DateField})
	nacionalidade = db.Column(db.String(200),info={'label': 'Nacionalidade'})
	ufNascimento  = db.Column(db.String(2),info={'label': 'UF Nascimento', 'choices': [(c.value, c.name) for c in UF]})
	nomeMae = db.Column(db.String(200),info={'label': 'Mãe'})
	nomePai = db.Column(db.String(200),info={'label': 'Pai'})
	naturalidade = db.Column(db.String(200),info={'label': 'Naturalidade'})
	tipoSanguineo = db.Column(db.String(3),info={'label': 'Tipo Sanguíneo', 'choices': [(c.name, c.value) for c in TipoSanguineo]})
	sexo  = db.Column(db.String(1),info={'label': 'Sexo', 'choices': [(c.name, c.value) for c in Sexo]})
	possuiDeficiencia = db.Column(db.Boolean,info={'label': 'Possui Deficiência'})
	TipoDeficiencia = db.Column(db.String(200),info={'label': 'Tipo da Deficiência'})
	raca_cor = db.Column(db.String(200),info={'label': 'Raça/Cor'})
	endereco_id = db.Column(db.Integer, db.ForeignKey('enderecos.id'),info={'label': 'Endereço'})
	endereco = db.relationship("Endereco")
	telefone1_id = db.Column(db.Integer, db.ForeignKey('telefones.id'),info={'label': 'Telefone 1'})
	telefone1 = db.relationship("Telefone", foreign_keys=[telefone1_id])
	telefone2_id = db.Column(db.Integer, db.ForeignKey('telefones.id'),info={'label': 'Telefone 2'})
	telefone2 = db.relationship("Telefone", foreign_keys=[telefone2_id])
	email_Pessoal = db.Column(db.String(120), unique=True,info={'label': 'E-mail Pessoal'})
	email_Institucional = db.Column(db.String(120), unique=True,info={'label': 'E-mail Institucional'})
	curriculumLattes = db.Column(db.String(120), unique=True,info={'label': 'Curriculum Lattes'})
	rg_Numero = db.Column(db.String(200),info={'label': 'Nº'})
	rg_OrgaoExpedidor = db.Column(db.String(200),info={'label': 'Org. Exp.'})
	rg_UF = db.Column(db.String(2),info={'label': 'UF', 'choices': [(c.value, c.name) for c in UF]})
	rg_Emissao = db.Column(db.DateTime,info={'label': 'Emissão','form_field_class': DateField})
	cpf = db.Column(db.String(200), unique=True,info={'label': 'CPF'})
	pis_pasep = db.Column(db.String(20),info={'label': 'PIS/PASEP'})
	tituloEleitor = db.Column(db.String(20),info={'label': 'Nº'})
	tituloEleitor_UF = db.Column(db.String(2),info={'label': 'UF', 'choices': [(c.value, c.name) for c in UF]})
	tituloEleitor_Zona = db.Column(db.String(5),info={'label': 'Zona'})
	tituloEleitor_Secao = db.Column(db.String(5),info={'label': 'Seção'})
	tituloEleitor_Emissao = db.Column(db.DateTime,info={'label': 'Emissão','form_field_class': DateField})
	certificadoMilitar = db.Column(db.String(20),info={'label': 'Nº'})
	certificadoMilitar_Orgao = db.Column(db.String(200),info={'label': 'Orgão'})
	certificadoMilitar_Serie = db.Column(db.String(20),info={'label': 'Série'})
	passaporte = db.Column(db.String(20),info={'label': 'Passaporte'})
	pagamento_Banco = db.Column(db.String(5),info={'label': 'Banco'})
	pagamento_Agencia = db.Column(db.String(12),info={'label': 'Agência'})
	pagamento_Conta = db.Column(db.String(12),info={'label': 'Conta'})
	pagamento_TipoConta = db.Column(db.String(2),info={'label': 'Tipo Conta', 'choices': [(c.name,c.value) for c in TipoContaBancaria]})
	cargosfuncoesgratificadas = db.relationship("PessoaCargoFuncaoGratificada", backref="pessoa")
	titulos = db.relationship("Titulo", backref="pessoa",info={'label': 'Títulos'})
	progressoes = db.relationship("Progressao", backref="pessoa",info={'label': 'Progressões'})
	
	jornada = db.Column(db.String(2),info={'label': 'Jornada', 'choices': [(c.name, c.value) for c in JornadaTrabalho]})
	
	campusLotacao_id  = db.Column(db.Integer, db.ForeignKey('campus.id'),info={'label': 'Campus Lotação'})
	campusLotacao = db.relationship("Campus", foreign_keys=[campusLotacao_id])
	campusExercicio_id  = db.Column(db.Integer, db.ForeignKey('campus.id'),info={'label': 'Campus Exercício'})
	campusExercicio = db.relationship("Campus", foreign_keys=[campusExercicio_id])
	
	cargo_id = db.Column(db.Integer, db.ForeignKey('cargos.id'),info={'label': 'Cargo'})
	cargo = db.relationship("Cargo")
	
		
	def __repr__(self):
		return '<Pessoa %r>' % self.nome
				
class ClasseNivel(db.Model):
	__tablename__ = 'classesniveis'
	id = db.Column(db.Integer, primary_key = True)
	tipoServidor = db.Column(db.String(2),info={'label': 'Tipo Servidor', 'choices': [(c.name, c.value) for c in TipoServidor]})
	classe = db.Column(db.String(10),info={'label': 'Classe'})
	nivel = db.Column(db.String(5),info={'label': 'Nível'})
	
	def __repr__(self):
		return '<Classe/Nivel %r - %r>' % self.classe, self.nivel
		
	def __str__(self):
		return '%r - %r' % self.classe, self.nivel

class Progressao(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	classenivel_id = db.Column(db.Integer, db.ForeignKey('classesniveis.id'))
	classenivel = db.relationship('ClasseNivel')
	dataInicio = db.Column(db.DateTime,info={'label': 'Início','form_field_class': DateField})
	dataTermino = db.Column(db.DateTime,info={'label': 'Término','form_field_class': DateField})
	
	pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))
	
	
class Endereco(db.Model):
	__tablename__ = 'enderecos'
	id = db.Column(db.Integer, primary_key = True)
	logradouro  = db.Column(db.String(200),info={'label': 'Logradouro'})
	numero  = db.Column(db.String(10),info={'label': 'Nº'})
	complemento  = db.Column(db.String(200),info={'label': 'Compl.'})
	bairro  = db.Column(db.String(200),info={'label': 'Bairro'})
	municipio  = db.Column(db.String(200),info={'label': 'Município'})
	pais  = db.Column(db.String(100),info={'label': 'País'})
	estado = db.Column(db.String(2),info={'label': 'UF', 'choices': [(c.name, c.value) for c in UF]})
	cep = db.Column(db.String(10),info={'label': 'CEP'})
	
	
class Telefone(db.Model):
	__tablename__ = 'telefones'
	id = db.Column(db.Integer, primary_key = True)
	ddd = db.Column(db.String(2),info={'label': 'DDD'})
	numero = db.Column(db.String(12),info={'label': 'Nº'})
	ramal = db.Column(db.String(8),info={'label': 'Ramal'})	
	
	#pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'))

class Cargo(db.Model):	
	__tablename__ = 'cargos'
	id = db.Column(db.Integer, primary_key = True)
	tipoServidor = db.Column(db.String(2),info={'label': 'Tipo Servidor', 'choices': [(c.name, c.value) for c in TipoServidor]})
	nome = db.Column(db.String(200),info={'label': 'Nome'})
	

class CargoFuncaoGratificada(db.Model):	
	__tablename__ = 'cargosfuncoesgratificadas'
	id = db.Column(db.Integer, primary_key = True)
	classe   = db.Column(db.String(2),info={'label': 'Classe', 'choices': [(c.name, c.value) for c in ClasseCargoFuncao]}) 
	nivel    = db.Column(db.String(5),info={'label': 'Nível'}) 
	
class PessoaCargoFuncaoGratificada(db.Model):
	__tablename__ = 'pessoascargosfuncoesgratificadas'
	id = db.Column(db.Integer, primary_key = True)
	dataInicio = db.Column(db.DateTime,info={'label': 'Início','form_field_class': DateField})
	dataTermino = db.Column(db.DateTime,info={'label': 'Término','form_field_class': DateField})
	descricao = db.Column(db.String(120),info={'label': 'Descrição'})
		
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
	titulo = db.Column(db.String(3),info={'label': 'Título', 'choices': [(c.name, c.value) for c in Titulacao]})
	area = db.Column(db.String(120),info={'label': 'Área'}) 
	instituicao = db.Column(db.String(120),info={'label': 'Instituição'})
	dataInicio = db.Column(db.DateTime,info={'label': 'Início','form_field_class': DateField})
	dataTermino = db.Column(db.DateTime,info={'label': 'Término','form_field_class': DateField})
	
	pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoas.id'),info={'label': 'Servidor'})

	def __repr__(self):
		return '<Titulo %r>' % self.titulo

