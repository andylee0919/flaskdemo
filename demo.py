from flask import Flask 
from flask import render_template
from random import randint
app = Flask(__name__)

@app.route('/')
def home():
    return "This is my home page"

if __name__ == '__main__':
    app.run()