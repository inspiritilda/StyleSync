from flask import Flask, url_for, render_template, request, Blueprint, redirect, flash
from db import db
from models import User
from pathlib import Path
from werkzeug.security import generate_password_hash, check_password_hash


html_routes_bp = Blueprint("html", __name__)

@html_routes_bp.route("/home")
def home():
    return render_template("/html/index.html")