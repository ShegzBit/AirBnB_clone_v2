#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.base_model import (Base,
                               Column, String, Integer,
                               relationship, ForeignKey)

from models.state import BaseModel


import os
db = os.getenv("HBNB_TYPE_STORAGE")

is_db = db == "db"


class Review(*(BaseModel, Base) if is_db else (BaseModel,)):
    """ Review classto store review information """
    if is_db:
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        user = relationship("User", back_populates="reviews")
        place = relationship("Place", back_populates="reviews")
    else:
        place_id = ""
        user_id = ""
        text = ""
