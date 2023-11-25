#!/usr/bin/python3
"""Test cases for amenity model"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test class for the model amenity"""

    def __init__(self, *args, **kwargs):
        """ initializing attributes"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """tests the ameninty's name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
