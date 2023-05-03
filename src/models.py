import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(200), nullable=False)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    password = Column(String(200), nullable=False)
    user_name = Column(String(200))


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(80))
    description = Column(String(80))
    rotation_period = Column(Integer)
    diameter = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    terrain = Column(String(80))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    description = Column(String(200))
    gender = Column(String(60))
    mass = Column(Integer)
    name = Column(String(60))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
