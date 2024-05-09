from flask import Flask, url_for, render_template, request, Blueprint, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import os


html_routes_bp = Blueprint("html", __name__)

@html_routes_bp.route("/home")
def home():
    return render_template("/html/index.html")

@html_routes_bp.route("/homepage")
def homepage():
    return render_template("/html/home.html")

@html_routes_bp.route("/newoutfit")
def newoutfit():
    return render_template("/html/newoutfit.html")

@html_routes_bp.route("/wardrobe")
def wardrobe():
    #this is used to populate the html wardrobe grid with pictures in assets folder - temporary
    folder_path = 'static/Assets'
    image_files = [filename for filename in os.listdir(folder_path)
                   if filename.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    image_urls = [url_for('static', filename=f'Assets/{filename}') for filename in image_files]
    print(image_urls)

    return render_template("/html/wardrobe.html", image_urls=image_urls)