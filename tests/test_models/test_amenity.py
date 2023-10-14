#!/usr/bin/python3

''' This model contains unit tests for the class Amenity '''

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    ''' Tests the class Amenity '''

    def setUp(self):
        ''' Set up '''
        self.amenity = Amenity()

    def tearDown(self):
        ''' Tear down '''
        del self.amenity

    def test_amenity_creation(self):
        ''' Tests if Amenity is created and all elements are initialised
            properly '''

        self.assertIsInstance(self.amenity, Amenity)
        self.assertEqual(self.amenity.name, "")

    def test_amenity_assignment(self):
        ''' Tests if things are assigned properly '''

        self.amenity.name = "Couch"

        self.assertEqual(self.amenity.name, "Couch")


if __name__ == "__main__":
    unittest.main()
