from flask import Blueprint #Import Blueprint to split views

auth = Blueprint("auth", __name__)

#Create Login logic
@auth.route('/login')
def login():
    return "<p>Login</p>"

#Create Logout logic
@auth.route('/logout')
def logout():
    pass

#Create Sign up logic
@auth.route('/sign-up')
def sign_up():
    pass