#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel

from models.base_model import (Base, Table,
                               Column, String, Integer, Float,
                               relationship, ForeignKey)

import os

db = os.getenv("HBNB_TYPE_STORAGE")
is_db = db == "db"

place_table = Table("place_amenity", Base.metadata,
                    Column("place_id", String(60),
                           ForeignKey("places.id"), primary_key=True),
                    Column("amenity_id", String(60),
                           ForeignKey("amenities.id"), primary_key=True)
                    )


class Place(*(BaseModel, Base) if is_db else (BaseModel,)):
    """ A place to stay """

    if is_db:
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        cities = relationship("City", back_populates="places",
                              cascade="all, delete")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 back_populates="place_amenities",
                                 viewonly=False)
        reviews = relationship("Review", back_populates="place",
                               cascade="all, delete")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def cities(self):
            cities = models.storage.all(City)
            my_cities = list(filter(lambda review: review.place_id ==
                                    self.id, cities))
            return my_cities

        @property
        def reviews(self):
            reviews = models.storage.all(Review)
            my_reviews = list(filter(lambda review:
                                     review.place_id == self.id, reviews))
            return my_reviews
