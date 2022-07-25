from flask import Flask

app = Flask("hello")

@app.route("/") # raiz 
@app.route("/hello")
def hello():
    return "Hello world !! Again"

@app.route("/meucontato")
def meuContato():
    return "Emilia Brasilio, ebrasilio@jaja.com"