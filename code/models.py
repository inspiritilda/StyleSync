from sqlalchemy import (
    Boolean,
    Float,
    Numeric,
    ForeignKey,
    Integer,
    String,
    DECIMAL,
    DateTime,
    DATETIME,
)
from sqlalchemy.orm import mapped_column, relationship
from db import db
import math
from sqlalchemy.sql import functions as func


class User(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(200), nullable=False)
    # phone = mapped_column(String(20), nullable=False)
    email = mapped_column(String(200), nullable=False, unique=True)
    password = mapped_column(String(200), nullable=False)

    def _tojson(self):
        return {
            "id": self.id,
            "name": self.name
        }

# Outfit Table
class Outfit(db.Model):
    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(Integer, ForeignKey('User.id'), nullable=False)
    date = mapped_column(DATETIME, nullable=False)
    rating = mapped_column(Integer, nullable=True)
    layer1 = mapped_column(Integer, ForeignKey('Layer1.id'), nullable=True)
    layer2 = mapped_column(Integer, ForeignKey('Layer2.id'), nullable=True)
    layer3 = mapped_column(Integer, ForeignKey('Layer3.id'), nullable=True)

# After creating the below categories for db, we need to add the foreign keys into Outfit Table

class weather(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(500), nullable=False)

class colour(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(500), nullable=False)

class feeling(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(500), nullable=False)

class style(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(500), nullable=False)

# Layer 1 Table (Shirt)
class Layer1(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(500), nullable=False)
    style_id = mapped_column(Integer, ForeignKey('style.id'))
    feeling_id = mapped_column(Integer, ForeignKey('feeling.id'))
    colour_id = mapped_column(Integer, ForeignKey('colour.id'))
    weather_id = mapped_column(Integer, ForeignKey('weather.id'))

# Layer 2 Table (Sweater)

# Layer 3 Table (Jacket)

# LegWear

# FootWear (Socks)

# ShoeWear

# Accessory 1

# Accessory 2

