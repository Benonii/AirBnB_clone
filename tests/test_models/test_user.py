#!/usr/bin/python3

''' This module contains tests for the class User '''

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    ''' Tests the class User '''

    def setUp(self):
        ''' Set up '''
        self.user = User()

    def tearDown(self):
        ''' Tear down '''
        del self.user

    def test_user_creation(self):
        ''' Tests if user is created and all elements are empty strings '''
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")

    def test_user_assignment(self):
        ''' Tests if things are assigned correctly '''

        self.user.first_name = "Benoni"
        self.user.last_name = "Esckinder"
        self.user.email = "Benoni123@email.com"
        self.user.password = "########"

        self.assertEqual(self.user.first_name, "Benoni")
        self.assertEqual(self.user.last_name, "Esckinder")
        self.assertEqual(self.user.email, "Benoni123@email.com")
        self.assertEqual(self.user.password, "########")


if __name__ == '__main__':
    unittest.main()
