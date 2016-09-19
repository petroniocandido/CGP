from flask import Flask, render_template
from flask import Blueprint

from DomainModel import db,Setor

setores = Blueprint('setores', __name__)

@setores.route('/listar/')
def setoresListar():
	setores = Setor.query.all()
	return render_template('listarSetores.html',setores = setores)
  
@setores.route('/editar/<int:id>')
def setorEditar():
	if id == 0:
		setor = Setor("","")
	else
		setor = Setor.get(id)
	return render_template('editarSetor.html',setor=setor)

