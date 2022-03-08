from flask import Blueprint #Import Blueprint to split views

views = Blueprint("views", __name__)

@views.route('/') #Binds route to a function
def home():
    return "<h1>Test</h1>"