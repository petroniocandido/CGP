from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import enum

#pessoas_enderecos = Table('pessoas_enderecos', Base.metadata,
#    Column('pessoa_id', Integer, ForeignKey('Pessoa.id')),
#    Column('endereco_id', Integer, ForeignKey('Endereco.id'))
#)


class Pessoa(Model):
	__tablename__ = 'pessoas'
	id = Column(Integer, primary_key = True)
	nome = Column(String(200), unique=True)
	matricula = Column(String(12), unique=True)
	matriculaOrigem  = Column(String(12), unique=True)
	identificacaoUnica = Column(String(12), unique=True)
	tipoServidor = Column(Enum(TipoServidor))
	situacaoServidor = Column(Enum(SituacaoServidor))
	dataCadastroSiape = Column(DateTime)
	dataNascimento = Column(DateTime)
	estadoCivil  = Column(Enum(EstadoCivil))
	dataPrimeiroEmprego = Column(DateTime)
	nacionalidade = Column(String(200))
	ufNascimento  = Column(Enum(UF))
	nomeMae = Column(String(200))
	nomePai = Column(String(200))
	naturalidade = Column(String(200))
	tipoSanguineo = Column(Enum(TipoSanguineo))
	sexo  = Column(Enum(Sexo))
	possuiDeficiencia = Column(Boolean)
	TipoDeficiência = Column(String(200))
	raca_cor = Column(String(200))
	enderecos = relationship("Endereco", back_populates="pessoa")
	telefones = relationship("Telefone", back_populates="pessoa")
	email_Pessoal = Column(String(120), unique=True)
	email_Institucional  = Column(String(120), unique=True)
	rg_Numero = Column(String(200))
	rg_OrgaoExpedidor = Column(String(200))
	rg_UF = Column(Enum(UF))
	rg_Emissao = Column(DateTime)
	cpf = Column(String(200), unique=True)
	pis_pased = Column(String(20))
	tituloEleitor = Column(String(20))
	tituloEleitor_UF = Column(Enum(UF))
	tituloEleitor_Zona = Column(String(5))
	tituloEleitor_Secao = Column(String(5))
	tituloEleitor_Emissao = Column(DateTime)
	certificadoMilitar = Column(String(20))
	certificadoMilitar_Orgao = Column(String(200))
	certificadoMilitar_Serie = Column(String(20))
	passaporte = Column(String(20))
	pagamento_Banco = Column(String(5))
	pagamento_Agencia = Column(String(12))
	pagamento_Conta = Column(String(12))
	pagamento_TipoConta = Column(Enum(TipoContaBancaria))
	cargos = relationship("Cargo", back_populates="pessoa")
	funcoes = relationship("Funcao", back_populates="pessoa")
	titulos = relationship("Titulos", back_populates="pessoa")
	progressoes = relationship("Progressao", back_populates="pessoa")
	
	jornada = Column(Enum(JornadaTrabalho))
	
	def __init__(self,logradouro, numero, complemento, bairro, municipio, pais, estado, cep, pessoa)
		self.logradouro = logradouro
		self.numero = numero
		self.complemento = complemento
		self.bairro = bairro
		self.municipio = municipio
		self.pais = pais
		self.estado = estado
		self.cep = cep
		self.pessoa = pessoa
		
	def __repr__(self):
        return '<Pessoa %r>' % self.nome
        	
class ClasseNivel
	__tablename__ = 'classesniveis'
	id = Column(Integer, primary_key = True
	classe = Column(String(5))
	nivel = Column(Integer)
	
	def __init__(self,classe,nivel)
		 self.classe = classe
		 self.nivel = nivel
	
	def __repr__(self):
        return '<Setor %r>' % self.nome

class Progressao(Model):
	id = Column(Integer, primary_key = True
	classenivel_id = Column(Integer, ForeignKey('ClasseNivel.id'))
	classenivel = relationship('ClasseNivel')
	dataInicio = Column(DateTime)
	dataTermino = Column(DateTime)
	
	pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship('Pessoa',  backref=backref('progressoes', lazy='dynamic'))
    
    def __init__(self,classenivel,dataInicio,dataTermino,pessoa)
		self.classenivel = classenivel
		self.dataInicio = dataInicio
		self.dataTermino = dataTermino
		self.pessoa = pessoa
    
    def __repr__(self):
        return '<Setor %r>' % self.nome

class Endereco(Model):
	__tablename__ = 'enderecos'
	id = Column(Integer, primary_key = True)
	logradouro  = Column(String(200))
	numero  = Column(String(10))
	complemento  = Column(String(200))
	bairro  = Column(String(200))
	municipio  = Column(String(200))
	pais  = Column(String(100))
	estado = Column(Enum(UF))
	cep = Column(String(10))
	
	pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship('Pessoa',  backref=backref('enderecos', lazy='dynamic'))
	
	def __init__(self,logradouro, numero, complemento, bairro, municipio, pais, estado, cep, pessoa)
		self.logradouro = logradouro
		self.numero = numero
		self.complemento = complemento
		self.bairro = bairro
		self.municipio = municipio
		self.pais = pais
		self.estado = estado
		self.cep = cep
		self.pessoa = pessoa
		
	def __repr__(self):
        return '<Setor %r>' % self.nome
	
class Telefone(Model):
	__tablename__ = 'telefones'
	id = Column(Integer, primary_key = True)
	ddd = Column(String(2))
	numero = Column(String(12))
	ramal = Column(String(8))
	fixo
	celular
	prestadora
	
	pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship('Pessoa',  backref=backref('enderecos', lazy='dynamic'))
	
	def __init__(self, ddd, numero, ramal, fixo, celular, prestadora):
        self.ddd = ddd
        self.numero = numero
        self.ramal = ramal
        self.fixo = fixo
        self.celular = celular
        self.prestadora = prestadora

    def __repr__(self):
        return '<Setor %r>' % self.nome
	
class Cargo(Model):
	__tablename__ = 'cargos'
	id = Column(Integer, primary_key = True)
	cargo
	classe
	padrao
	dataPosse = Column(DateTime)
	dataSaida = Column(DateTime)
	codigoVaga
	ingresso = Column(DateTime)
	exercicio = Column(DateTime)
	
	pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship('Pessoa',  backref=backref('enderecos', lazy='dynamic'))
	
	def __init__(self, sigla, codigo, nome, dataIngresso, dataSaida, atividade):
        self.sigla = sigla
        self.codigo = codigo
        self.nome = nome
        self.dataIngresso = dataIngresso
        self.dataSaida = dataSaida
        self.atividade = atividade

    def __repr__(self):
        return '<Setor %r>' % self.nome
	
class Funcao(Model):
	__tablename__ = 'funcoes'
	id = Column(Integer, primary_key = True)
	sigla = Column(String(120), unique=True)
	codigo = Column(String(120), unique=True)
	nome = Column(String(120), unique=True)
	dataIngresso = Column(DateTime)
	dataSaida = Column(DateTime)
	atividade = Column(String(120), unique=True)
	
	pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship('Pessoa',  backref=backref('enderecos', lazy='dynamic'))
	
	def __init__(self, sigla, codigo, nome, dataIngresso, dataSaida, atividade):
        self.sigla = sigla
        self.codigo = codigo
        self.nome = nome
        self.dataIngresso = dataIngresso
        self.dataSaida = dataSaida
        self.atividade = atividade

    def __repr__(self):
        return '<Setor %r>' % self.nome
	
class Setor(Model):
	__tablename__ = 'setores'
	id = Column(Integer, primary_key = True)
	sigla = Column(String(120), unique=True)
	nome = Column(String(120), unique=True)
	
	def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome

    def __repr__(self):
        return '<Setor %r>' % self.nome
        
class Titulos(Model):
	__tablename__ = 'titulos'
	id = Column(Integer, primary_key = True)
	titulo = Column(Enum(Titulacao))
	area = Column(String(120)) 
	instituicao = Column(String(120))
	dataInicio = Column(DateTime)
	dataTermino = Column(DateTime)
	
	pessoa_id = Column(Integer, ForeignKey('Pessoa.id'))
    pessoa = relationship('Pessoa',  backref=backref('titulos', lazy='dynamic'))
	
	def __init__(self, titulo, area, instituicao, dataInicio, dataTermino, pessoa):
        self.titulo = titulo
        self.area = area
        self.instituicao = instituicao
        self.dataInicio = dataInicio
        self.dataTermino = dataTermino
        self.pessoa = pessoa

    def __repr__(self):
        return '<Setor %r>' % self.nome


class TipoServidor(Enum):
	TAE = "Técnico-Administrativo"
	DOC = "Docente"
	
class SituacaoServidor(IntEnum):
	Ativo = 1
	Pensionista = 2


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

