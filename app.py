from flask import Flask, render_template, url_for

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

app.config['SECRET_KEY'] = "1!aA2@sS3#dD4$fF5%gG"

from pessoas.controller import pessoas
from setores.controller import setores
from campus.controller import campus
from classenivel.controller import classenivel
from cargos.controller import cargos
from titulos.controller import titulos
from progressoes.controller import progressoes

app.register_blueprint(pessoas, url_prefix='/pessoas')
app.register_blueprint(setores, url_prefix='/setores')
app.register_blueprint(campus, url_prefix='/campus')
app.register_blueprint(classenivel, url_prefix='/classenivel')
app.register_blueprint(cargos, url_prefix='/cargos')
app.register_blueprint(titulos, url_prefix='/titulos')
app.register_blueprint(progressoes, url_prefix='/progressoes')

@app.route('/')
def home():
  return render_template('listarPessoas.html')
  
 
if __name__ == '__main__':
  app.run(debug=True)
  
url_for('static', filename='local.css')

#app.run()
