#!/usr/bin/python3
"""Test cases for file storage"""
import unittest
import os
from models.user import User
from models import storage
from models.state import State


@unittest.skipIf((os.getenv('HBNB_TYPE_STORAGE') == 'db'),
                 "Unsupported action")
class TestFileStorage(unittest.TestCase):
    """test class for filestorage"""

    def setUp(self):
        """set up environment"""
        dummy_list = []
        for key in storage._FileStorage__objects.keys():
            dummy_list.append(key)
        for key in dummy_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """discard environemnt and all its files"""
        try:
            os.remove('file.json')
        except:
            pass

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
        """tests all method for"""
        another_state = State()
        another_state.save()
        all_states_list = storage.all(State)
        self.assertIsInstance(all_states_list, dict)

        i = 0
        for obj in all_states_list.values():
            if type(obj) == State:
                i += 1
        self.assertEqual(i, 1)

    def test_save(self):
        """tests the save method"""
        new_user = User()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_new(self):
        """tests new method"""
        new_usr = User()
        new_usr.save()
        for obj in storage.all().values():
            dummy = obj
        self.assertTrue(dummy is obj)

    def test_reload(self):
        """test reload method"""
        new_state2 = State()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new_state2.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """reload from an empty file"""
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()
