from flask import Flask

app = Flask(__name__)


@app.route('/')
#hello
def hello():
    return '<h1>Hello, World!</h1>'