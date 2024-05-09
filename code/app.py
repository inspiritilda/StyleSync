from flask import Flask, url_for, session, redirect
from db import db
from pathlib import Path
from routes import auth_routes_bp, html_routes_bp
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = "supersecret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.instance_path = Path("./data").resolve()

# Initialize the database
db.init_app(app)
app.register_blueprint(auth_routes_bp, url_prefix="/")
app.register_blueprint(html_routes_bp, url_prefix="/views")


if __name__ == "__main__":
    app.run(debug=True, port=8888)
