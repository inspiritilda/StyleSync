import csv
from app import app
from db import db
from models import User
import random
from sqlalchemy.sql import functions as func


def create_tables():
    with app.app_context():
        db.create_all()


def drop_tables():
    with app.app_context():
        db.drop_all()

ld

if __name__ == "__main__":
    drop_tables()
    create_tables()
    print("Database seeded")
