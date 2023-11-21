#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import (BaseModel, Base,
                               Column, String, Integer, relationship)
import models

import os

db = os.getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """ State class """

    # Table Definition

    if db == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
    else:
        name = ""
    if db == "db":
        cities = relationship('City', back_populates="state", cascade="all, delete")
    if db == "FileStorage":
        @cities.getter
        def cities(self):
            """
            Implements the correct getting requirement for both
            FIleStorage
            """
            city_list = []
            objects = storage.all(City).values()
            for obj in objects:
                if obj.id == self.id:
                    cities.append(id)
            return city_list
