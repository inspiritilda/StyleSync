from flask import Flask, url_for, render_template, request, Blueprint, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
<<<<<<< HEAD
from flask_login import login_required,current_user
=======
import os

>>>>>>> origin/dev

html_routes_bp = Blueprint("html", __name__)

@html_routes_bp.route("/home")
@login_required
def home():
    print(current_user)
    return render_template("/html/wardrobe.html", user=current_user)

@html_routes_bp.route("/homepage")
@login_required
def homepage():
    return render_template("/html/home.html", user  = current_user)

@html_routes_bp.route("/newoutfit")
@login_required
def newoutfit():
    folder_path = 'static/pics'
    image_files = [filename for filename in os.listdir(folder_path)
                   if filename.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    image_urls = [url_for('static', filename=f'pics/{filename}') for filename in image_files]
    print(image_urls)
    return render_template("/html/newoutfit.html", image_urls=image_urls)

@html_routes_bp.route("/wardrobe")
@login_required
def wardrobe():
<<<<<<< HEAD

    return render_template("/html/wardrobe.html", user = current_user)
=======
    #this is used to populate the html wardrobe grid with pictures in assets folder - temporary
    folder_path = 'static/pics/demopics'
    image_files = [filename for filename in os.listdir(folder_path)
                   if filename.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    image_urls = [url_for('static', filename=f'pics/demopics/{filename}') for filename in image_files]
    print(image_urls)

    return render_template("/html/wardrobe.html", image_urls=image_urls)
>>>>>>> origin/dev
