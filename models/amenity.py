#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import (Base,
                               Column, String, Integer,
                               relationship, ForeignKey)

from models.state import BaseModel
# from models.place import place_table

import os
db = os.getenv("HBNB_TYPE_STORAGE")

is_db = db == "db"


class Amenity(*(BaseModel, Base) if is_db else (BaseModel,)):
    """
    Class for the amenities a place has
    """
    if is_db:
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
                                       "Place", secondary="place_amenity",
                                       back_populates="amenities",
                                       viewonly=False
                                       )
    else:
        name = ""
