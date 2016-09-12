from flask import Flask, render_template

app = Flask(__name__)

#@app.route("/")
#def hello_world():
#    return "Hello World! <strong>I am learning Flask</strong>", 200

@app.route('/')
def home():
  return render_template('home.html')
 
if __name__ == '__main__':
  app.run(debug=True)

#app.run()
