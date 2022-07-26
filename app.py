from flask import Flask, render_template, request
from datetime import datetime

app = Flask("hello")

# mock ==> simulação
posts = [
    {
        "title": "My first post",
        "body": "Here, my text",
        "author": "Me",
        "created": datetime(2022,7,25)
    },
    {
        "title": "My second post",
        "body": "Here, my text again",
        "author": "Not Me",
        "created": datetime(2022,7,26)  
    }
]

@app.route("/") # raiz 
def index():
    return render_template("index.html", posts=posts)