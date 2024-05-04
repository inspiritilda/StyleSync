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


