from flask import Flask, url_for, render_template, request, Blueprint,redirect
from db import db
from models import User
from pathlib import Path
from werkzeug.security import generate_password_hash, check_password_hash


auth_routes_bp = Blueprint("authorization", __name__)


@auth_routes_bp.route("/")
def home():
    return render_template("/auth/login.html")

@auth_routes_bp.route("/auth/register")
def register():
    return render_template("/auth/signup.html")
@auth_routes_bp.route("/auth/register", methods=["POST"])
def signup():
    email = request.form.get("email")
    name = request.form.get("name")
    passwords = request.form.get("password")
    print(email)
    print(name)
    print(passwords)
    if not email or not name or not passwords:
        return redirect(url_for("authorization.register"))
    # if len(passwords) < 8:
    #     return redirect(url_for("authorization.register"))
    if email == "" or name == "" or passwords == "":
        return redirect(url_for("authorization.register"))
    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(
        email=email,
        name=name,
        password=generate_password_hash(passwords, method="scrypt"),
    )

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("authorization.home"))   
@auth_routes_bp.route("/auth/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    print(email)    
    print(password)
    statement = db.select(User).where(User.email == email)
    user = db.session.execute(statement).scalar()
    print(check_password_hash(user.password, password))
    if not  check_password_hash(user.password, password):
        return redirect(url_for("authorization.register"))
    return "Logged in!"

