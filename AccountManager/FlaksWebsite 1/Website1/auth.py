from flask import Blueprint #Import Blueprint to split views
from flask import render_template #Renders html templates created in the sperate files
from flask import request #Handles HTTP request
from flask import flash #Create message handling?

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
            flash("Email must be greater than 3 characters.", category="error")
        elif len(firstName) < 2:
            flash("First name must be greater than 1 character.", category="error")
        elif password1 != password2:
           flash("Paswords don't match.", category="error")
        elif len(password1) < 7:
            flash("Pasword must be at least 7 characters.", category="error")
        else:
            #Add the user
            flash("Account created.", category="success")

    return render_template("sign_up.html")