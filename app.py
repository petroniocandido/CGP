from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = "1!aA2@sS3#dD4$fF5%gG"

from pessoas.controller import pessoas
from setores.controller import setores
from campus.controller import campus

app.register_blueprint(pessoas, url_prefix='/pessoas')
app.register_blueprint(setores, url_prefix='/setores')
app.register_blueprint(campus, url_prefix='/campus')

@app.route('/')
def home():
  return render_template('listarPessoas.html')
  

 
if __name__ == '__main__':
  app.run(debug=True)

#app.run()
