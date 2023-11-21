#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from datetime import datetime
import os
import models

db_type = os.getenv("HBNB_TYPE_STORAGE")

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""


    if db_type == "db":
        id = Column(String(60), primary_key=True, default=uuid4)
        created_at = Column(Date, default=datetime.utcnow(), primary_key=True)
        updated_at = Column(Date, default=datetime.utcnow(), nullable=False)
    else:
        id = uuid4
        created_at = datetime.now()
        updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """
        Class constructor for base module
        Init the public instance attribute `id`
        loads an instance from kwargs dictionary
        args is never used
        """
        
        # loop through kwargs and set
        # attribute the attribute is not the id or __class__ or created_at
        for x, y in kwargs.items():
            if x not in ("__class__", "created_at", "updated_at"):
                setattr(self, x, y)
            elif x in ("created_at", "updated_at"):
                y = datetime.fromisoformat(y)
                setattr(self, x, y)
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
        models.storage.save()
