from flask import Flask

app = Flask("hello")

@app.route("/") # raiz 
@app.route("/hello")
def hello():
    return """<html>
    <h1><mark>"Hello world !! Again"</mark></h1>
    </html>"""

@app.route("/meucontato")
def meuContato():
    return """<html>
    <head>
    <title>Contatos</title>
    </head>
    <body>
    <h1>Emilia Brasilio</h1>
    <mark>ebrasilio@jaja.com"</mark>
    </body>
    </html>"""