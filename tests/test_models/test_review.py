#!/usr/bin/python3
"""TestCases for reviews"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Class to test review"""

    def __init__(self, *args, **kwargs):
        """initializing attributes """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """tests the place id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """tests the user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ tests the text"""
        new = self.value()
        self.assertEqual(type(new.text), str)
