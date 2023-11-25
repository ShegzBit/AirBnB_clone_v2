#!/usr/bin/python3
"""Test cases for file storage"""
import unittest
import os
from models.user import User
from models import storage
from models.state import State


@unittest.skipIf((os.getenv('HBNB_TYPE_STORAGE') == 'db'),
                 "Unsupported action")
class test_filestorage(unittest.TestCase):
    """test class for filestorage"""
    def test_delete_with_args(self):
        """tests the delete method with arguments passed"""
        new_state = State()
        new_state.save()
        self.assertTrue(new_state in storage.all().values())
        storage.delete(new_state)
        self.assertFalse(new_state in storage.all().values())

    def test_delete_without_args(self):
        """tests delete method method with no args passed"""
        new_user = User()
        new_user.save()
        self.assertTrue(new_user in storage.all().values())
        storage.delete()
        self.assertTrue(new_user in storage.all().values())

    def test_all(self):
        """tests all method if it returns one type of class"""
        all_states_list = storage.all(State)
        i = 0
        for obj in all_states_list.values():
            if type(obj) == State:
                i += 1
        self.assertEqual(i, 1)
