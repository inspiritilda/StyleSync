from flask import Flask, url_for, render_template, request
from db import db
from models import User
from pathlib import Path
from routes import auth_routes_bp
from werkzeug.security import generate_password_hash, check_password_hash

# from routes import finals_bp,api_customers_bp, api_products_bp, api_order_bp, htmls_bp
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.instance_path = Path("./data").resolve()
# Initialize the database
db.init_app(app)
app.register_blueprint(auth_routes_bp, url_prefix="/")



if __name__ == "__main__":
    app.run(debug=True, port=8888)
