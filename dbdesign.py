from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import and_
from sqlalchemy import create_engine, Column, String, Float, ForeignKey
import uuid

Base = declarative_base()
def generate_uuid():
    return str(uuid.uuid4())

#TAGS

# style tag
class styletag(Base):
    __tablename__ = 'Style'
    Style = Column(String, primary_key=True)

    def __init__(self, Style):
        self.Style = Style

# feeling tag
class feelingtag(Base):
    __tablename__ = 'Feeling'
    Feeling = Column(String, primary_key=True)

    def __init__(self, Feeling):
        self.Feeling = Feeling

# color tag
class colortag(Base):
    __tablename__ = 'Color'
    Color = Column(String, primary_key=True)

    def __init__(self, Color):
        self.Color = Color

# weather tag
class weathertag(Base):
    __tablename__ = 'Weather'
    Weather = Column(String, primary_key=True)

    def __init__(self, Weather):
        self.Weather = Weather


# CLOTHES

# 1st Layer
class Layer1(Base):
    __tablename__ = 'Layer1'
    L1 = Column(String, primary_key=True)
    Style = Column(String, ForeignKey("Style.Style"))
    Feeling = Column(String, ForeignKey("Feeling.Feeling"))
    Color = Column(String, ForeignKey("Color.Color"))
    Weather = Column(String, ForeignKey("Weather.Weather"))

    def __init__(self, L1, Style, Feeling, Color, Weather):
        self.L1 = L1
        self.Style = Style
        self.Feeling = Feeling
        self.Color = Color
        self.Weather = Weather


class Layer2(Base):
    __tablename__ = 'Layer2'
    L2 = Column(String, primary_key=True)
    Style = Column(String, ForeignKey("Style.Style"))
    Feeling = Column(String, ForeignKey("Feeling.Feeling"))
    Color = Column(String, ForeignKey("Color.Color"))
    Weather = Column(String, ForeignKey("Weather.Weather"))

    def __init__(self, L2, Style, Feeling, Color, Weather):
        self.L2 = L2
        self.Style = Style
        self.Feeling = Feeling
        self.Color = Color
        self.Weather = Weather


class LegWear(Base):
    __tablename__ = 'LegWear'
    LW = Column(String, primary_key=True)
    Style = Column(String, ForeignKey("Style.Style"))
    Feeling = Column(String, ForeignKey("Feeling.Feeling"))
    Color = Column(String, ForeignKey("Color.Color"))
    Weather = Column(String, ForeignKey("Weather.Weather"))

    def __init__(self, LW, Style, Feeling, Color, Weather):
        self.LW = LW
        self.Style = Style
        self.Feeling = Feeling
        self.Color = Color
        self.Weather = Weather


class ShoeWear(Base):
    __tablename__ = 'ShoeWear'
    SW = Column(String, primary_key=True)
    Style = Column(String, ForeignKey("Style.Style"))
    Feeling = Column(String, ForeignKey("Feeling.Feeling"))
    Color = Column(String, ForeignKey("Color.Color"))
    Weather = Column(String, ForeignKey("Weather.Weather"))

    def __init__(self, SW, Style, Feeling, Color, Weather):
        self.SW = SW
        self.Style = Style
        self.Feeling = Feeling
        self.Color = Color
        self.Weather = Weather


#outfit
class Outfit(Base):
    __tablename__ = 'Outfit'
    O = Column(String, primary_key=True)
    L1 = Column(String, ForeignKey("Layer1.L1"))
    L2 = Column(String, ForeignKey("Layer2.L2"))
    LW = Column(String, ForeignKey("LegWear.LW"))
    SW = Column(String, ForeignKey("ShoeWear.SW"))

    def __init__(self, O, L1, L2, LW, SW):
        self.O = O
        self.L1 = L1
        self.L2 = L2
        self.LW = LW
        self.SW = SW


def addstyle(session, Style):
    stag = styletag(Style)
    session.add(stag)
    session.commit()
    print("New style added")

def addfeeling(session, Feeling):
    ftag = feelingtag(Feeling)
    session.add(ftag)
    session.commit()
    print("New feeling added")

def addcolor(session, Color):
    ctag = colortag(Color)
    session.add(ctag)
    session.commit()
    print("New color added")

def addweather(session, Weather):
    wtag = weathertag(Weather)
    session.add(wtag)
    session.commit()
    print("New weather added")

def addlayer1(session, L1, Style, Feeling, Color, Weather):
    newcloth = Layer1(L1, Style, Feeling, Color, Weather)
    session.add(newcloth)
    session.commit()
    print("New cloth added to layer 1")

def addlayer2(session, L2, Style, Feeling, Color, Weather):
    newcloth = Layer2(L2, Style, Feeling, Color, Weather)
    session.add(newcloth)
    session.commit()
    print("New cloth added to layer 2")

def addlegwear(session, LW, Style, Feeling, Color, Weather):
    newcloth = LegWear(LW, Style, Feeling, Color, Weather)
    session.add(newcloth)
    session.commit()
    print("New cloth added to leg wear")

def addshoes(session, SW, Style, Feeling, Color, Weather):
    newcloth = ShoeWear(SW, Style, Feeling, Color, Weather)
    session.add(newcloth)
    session.commit()
    print("New shoes added")

def addoutfit(session, O, L1, L2, LW, SW):
    newoutfit = Outfit(O, L1, L2, LW, SW)
    session.add(newoutfit)
    session.commit()
    print("New outfilt added")

db = "sqlite:///prac1.db"
engine = create_engine(db)
Base.metadata.create_all(bind=engine)

session = sessionmaker(bind=engine)
session = session()
"""
# tag creation
Style = "Classic"
addstyle(session, Style)

Feeling = "Fancy"
addfeeling(session, Feeling)

Color = "Blue"
addcolor(session, Color)

Weather = "Cloudy"
addweather(session, Weather)


# cloth creation

L1 = "Black Sweater"
Style = "Casual"
Feeling = "Cool"
Color = "Black"
Weather = "Windy"
addlayer1(session, L1, Style, Feeling, Color, Weather)

L2 = "Raincoat"
Style = "Sporty"
Feeling = "Chill"
Color = "Yellow"
Weather = "Rainy"
addlayer2(session, L2, Style, Feeling, Color, Weather)

LW = "Cargo pants"
Style = "Street"
Feeling = "Cool"
Color = "Yellow"
Weather = "Rainy"
addlegwear(session, LW, Style, Feeling, Color, Weather)

SW = "Boots"
Style = "Sporty"
Feeling = "Cool"
Color = "Black"
Weather = "Rainy"
addshoes(session, SW, Style, Feeling, Color, Weather)

# outfit creation
O = "Rains"
L1 = "Black Sweater"
L2 = "Raincoat"
LW = "Cargo pants"
SW = "Boots"
addoutfit(session, O, L1, L2, LW, SW)
"""
# exist =session.query(Layer1, Layer2, LegWear, ShoeWear).filter((Layer1.L1==L1) & (Layer2.L2==L2) & (LegWear.LW==LW) & (ShoeWear.SW==SW)).all()
# print(len(exist))

    # existl1 =session.query(Layer1).filter(Layer1.L1==L1).all()
    # existl2 =session.query(Layer2).filter(Layer2.L2==L2).all()
    # existlw =session.query(LegWear).filter(LegWear.LW==LW).all()
    # existsw =session.query(ShoeWear).filter(ShoeWear.SW==SW).all()
    # if len(existl1) and len(existl2)>0 and len(existlw)>0 and len(existsw)>0:
    #     print("An outfit with the same clothes already exists.")
    # else:
    #     newoutfit = Outfit(O, L1, L2, LW, SW)
    #     session.add(newoutfit)
    #     session.commit()
    #     print("New outfilt added")
