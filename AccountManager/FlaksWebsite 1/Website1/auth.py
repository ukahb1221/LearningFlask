from flask import Blueprint #Import Blueprint to split views
from flask import render_template #Renders html templates created in the sperate files


auth = Blueprint("auth", __name__)

#Create Login logic
@auth.route('/login')
def login():
    return render_template("login.html", boolean =True)

#Create Logout logic
@auth.route('/logout')
def logout():
    pass

#Create Sign up logic
@auth.route('/sign-up')
def sign_up():
     return render_template("sign_up.html")