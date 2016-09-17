from flask import Flask, render_template
from flask import Blueprint


setores = Blueprint('setores', __name__)

@setores.route('/listar/')
def pessoaListar():
  return render_template('listarSetores.html')
  
@setores.route('/editar/')
def pessoaEditar():
  return render_template('editarSetor.html')

