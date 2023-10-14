#!/usr/bin/python3

'''This module contains unit tests for the class City '''

import unittest
from models.base_model import BaseModel
from models.city import City
from models.state import State


class TestCity(unittest.TestCase):
    ''' Tests the class City '''

    def setUp(self):
        ''' Set up '''
        self.city = City()
        self.state = State()

    def tearDown(self):
        ''' Tear down '''
        del self.city
        del self.state

    def test_city_creation(self):
        ''' Tests if city is created and all elements are initialised properly
        '''

        self.assertIsInstance(self.city, City)
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_city_assignment(self):
        ''' Tests if things are assigned properly '''

        self.city.state_id = self.state.id
        self.city.name = "Zootopia"

        self.assertEqual(self.city.state_id, self.state.id)
        self.assertEqual(self.city.name, "Zootopia")


if __name__ == "__main__":
    unittest.main()
