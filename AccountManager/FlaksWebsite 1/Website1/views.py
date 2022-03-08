from flask import Flask
from Website1 import app

@app.route('/')
@app.route('/home')
def home():
    return "Hello Flask!"
