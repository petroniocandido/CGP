from flask import Flask, render_template
from flask import Blueprint


pessoas = Blueprint('pessoas', __name__)

@pessoas.route('/listar/')
def pessoaListar():
  return render_template('listarPessoas.html')
  
@pessoas.route('/editar/')
def pessoaEditar():
  return render_template('editarPessoa.html')
