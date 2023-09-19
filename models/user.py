#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

        # Relationship to Place objects, cascade deletion on user deletion
        places = relationship("Place", backref="user", cascade="all, delete")

        # Relationship to Review objects, cascade deletion on user deletion
        reviews = relationship("Review", cascade='all, delete', backref="user")

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
