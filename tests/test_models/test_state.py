#!/usr/bin/python3
"""Testscases for state model"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Class for the test of the state model"""

    def __init__(self, *args, **kwargs):
        """initializing attributes"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """tests the state's name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
