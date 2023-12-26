#!/usr/bin/python3
""" State Module for HBNB project """
import models

from models.base_model import BaseModel, Base

import os

db = os.getenv("HBNB_TYPE_STORAGE")

is_db = db == "db"


class State(BaseModel, *(Base,) if is_db else ()):
    """ State class """

    if db == "db":
        from models.base_model import (Column,
                                       String, Integer, relationship)
        # Table Definition
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates="state",
                              cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """
            Implements the correct getting requirement for both
            FIleStorage
            """
            city_list = []
            objects = models.storage.all(models.city.City).values()
            for obj in objects:
                if obj.state_id == self.id:
                    city_list.append(obj)
            return city_list
