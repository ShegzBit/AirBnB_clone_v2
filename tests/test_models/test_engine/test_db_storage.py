#!/usr/bin/python3
"""tests for the db storage"""
import MySQLdb
import sys
import unittest
from console import HBNBCommand
from io import StringIO
from models.engine.db_storage import DBStorage
from models import storage
import os
from os import getenv
from models.user import User
from models.state import State


def get_table(table):
    """Get the number of rows in a db table
    """
    MY_USR = os.getenv('HBNB_MYSQL_USER')
    MY_PASSWD = os.getenv('HBNB_MYSQL_PWD')
    MY_DB = os.getenv('HBNB_MYSQL_DB')

    db = MySQLdb.connect(host='localhost', user=MY_USR, passwd=MY_PASSWD,
                           db=MY_DB)
    cursor = db.cursor()
    cursor.execute(f'SELECT * FROM {table};')
    return cursor.rowcount

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                         'Unsupported action')
class TestDBStorage(unittest.TestCase):
    """class for db test cases"""
    @classmethod
    def setUp(cls):
        """setting up environment"""
        pass
    @classmethod
    def tearDown(cls):
        """destroyin environment"""
        pass

    def test_db_creat(self):
        """test create method"""
        old_total = get_current('states')

        with patch('sys.stdout', new=StringIO()):
            HBNBCommand().onecmd('create State name="California"')
        new_total = get_current('states')
        self.assertEqual(new_total, old_total +1)
