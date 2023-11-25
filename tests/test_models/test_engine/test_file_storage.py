#!/usr/bin/python3
"""Test cases for file storage"""
import unittest
import os
from models.base_model import BaseModel
from models import storage


@unittest.skipIf((os.getenv('HBNB_TYPE_STORAGE') == 'db'),
                            "Unsupported action")
class test_filestorage(unittest.TestCase):
    """test class for filestorage"""
    def test_delete(self):
        """tests the delete method"""
        obj = BaseModel()
        obj.save()
        self.assertTrue(obj in storage.all().values())
        storage.delete(obj)
        self.assertFalse(obj in storage.all().values())
