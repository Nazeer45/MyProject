from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!\nThis is a python app deployment in Azure."
