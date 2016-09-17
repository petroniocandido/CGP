from flask import Flask, render_template

app = Flask(__name__)

from pessoas.controller import pessoas
from setores.controller import setores

app.register_blueprint(pessoas, url_prefix='/pessoas')
app.register_blueprint(setores, url_prefix='/setores')

@app.route('/')
def home():
  return render_template('listarPessoas.html')
  

 
if __name__ == '__main__':
  app.run(debug=True)

#app.run()
