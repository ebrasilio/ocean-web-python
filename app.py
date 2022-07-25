from flask import flask

app = Flask("hello")

app.route("/") # raiz 
def hello():
    return "Hello world !!"
