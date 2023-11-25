#!/usr/bin/python3
"""
Testcase for the user class
"""
class test_User(test_basemodel):
    """class for user test """

    def __init__(self, *args, **kwargs):
        """initializing attributes"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """method to check if the first name is a string"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """checks if user's last name is a string """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """checks if user's email is a string"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """checks if user's password is a string """
        new = self.value()
        self.assertEqual(type(new.password), str)
