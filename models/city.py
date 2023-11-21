#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import (Base,
                               Column, String, Integer, relationship, ForeignKey)

from models.state import BaseModel


import os
db = os.getenv("HBNB_TYPE_STORAGE")

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if db == "db":
        # Table definitions
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        state = relationship('State', back_populates="cities", cascade="all, delete")
    else:
        name = ""
        state_id=""


