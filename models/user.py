#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import (Base,
                               Column, String, Integer,
                               relationship, ForeignKey)

from models.state import BaseModel


import os
db = os.getenv("HBNB_TYPE_STORAGE")

is_db = db == "db"


class User(*(BaseModel, Base) if is_db else (BaseModel,)):
    """This class defines a user by various attributes"""
    if is_db:
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
