from flask import Blueprint #Import Blueprint to split views
from flask import render_template #Renders html templates created in the sperate files
from flask import request #Handles HTTP request

auth = Blueprint("auth", __name__)

#Create Login logic
@auth.route('/login', methods= ['GET', 'POST']) #Handle request 
def login():
    return render_template("login.html", boolean =True)

#Create Logout logic
@auth.route('/logout')
def logout():
    pass

#Create Sign up logic
@auth.route('/sign-up',  methods= ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            pass
        elif len(firstName) < 2:
            pass
        elif password1 != password2:
            pass
        elif len(password1) < 7:
            pass
        else:
            #Add the user
            pass

    return render_template("sign_up.html")