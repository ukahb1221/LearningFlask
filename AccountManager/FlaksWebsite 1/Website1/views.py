from flask import Blueprint #Import Blueprint to split views
from flask import render_template #Renders html templates created in the sperate files
views = Blueprint("views", __name__)

@views.route('/') #Binds route to a function
def home():
    return render_template("home.html")