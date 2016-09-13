from flask import Flask, render_template

app = Flask(__name__)

#@app.route("/")
#def hello_world():
#    return "Hello World! <strong>I am learning Flask</strong>", 200

@app.route('/')
def home():
  return render_template('listarPessoas.html')
  
@app.route('/pessoas/listar/')
def pessoaListar():
  return render_template('listarPessoas.html')
  
@app.route('/pessoas/editar/')
def pessoaEditar():
  return render_template('editarPessoa.html')
 
if __name__ == '__main__':
  app.run(debug=True)

#app.run()
