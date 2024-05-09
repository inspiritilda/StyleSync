from flask import Flask, url_for, render_template, request, Blueprint, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required,current_user

html_routes_bp = Blueprint("html", __name__)

@html_routes_bp.route("/home")
@login_required
def home():
    print(current_user)
    return render_template("/html/base.html", user=current_user)

@html_routes_bp.route("/homepage")
def homepage():
    return render_template("/html/home.html")

@html_routes_bp.route("/newoutfit")
def newoutfit():
    return render_template("/html/newoutfit.html")

@html_routes_bp.route("/wardrobe")
def wardrobe():
    return render_template("/html/wardrobe.html")