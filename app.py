from flask import Flask, redirect
import logging

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
file_handler = logging.FileHandler(filename='flask.log')
file_handler.setLevel(logging.NOTSET)
app.logger.addHandler(file_handler)
app.logger.info("Iniciando")

app.config['SECRET_KEY'] = "1!aA2@sS3#dD4$fF5%gG"

from login.controller import login
from logs.controller import logs
from perfis.controller import perfis
from permissoes.controller import permissoes
from pessoas.controller import pessoas
from setores.controller import setores
from campus.controller import campus
from classenivel.controller import classenivel
from cargos.controller import cargos
from titulos.controller import titulos
from progressoes.controller import progressoes
from cdfg.controller import cdfg

app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(logs, url_prefix='/logs')
app.register_blueprint(perfis, url_prefix='/perfis')
app.register_blueprint(permissoes, url_prefix='/permissoes')
app.register_blueprint(pessoas, url_prefix='/pessoas')
app.register_blueprint(setores, url_prefix='/setores')
app.register_blueprint(campus, url_prefix='/campus')
app.register_blueprint(classenivel, url_prefix='/classenivel')
app.register_blueprint(cargos, url_prefix='/cargos')
app.register_blueprint(titulos, url_prefix='/titulos')
app.register_blueprint(progressoes, url_prefix='/progressoes')
app.register_blueprint(cdfg, url_prefix='/cdfg')


@app.route('/')
def home():
    return redirect('login/login')


if __name__ == '__main__':
    app.run()

# url_for('static', filename='local.css')

# app.run()
