#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

st_type = os.getenv("HBNB_TYPE_STORAGE")

if st_type == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
