#!/usr/bin/python3

''' This module contanis unit tests of nt eclass Place '''

import unittest
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place


class TestPlace(unittest.TestCase):
    ''' Tests the class Place '''

    def setUp(self):
        ''' Set up '''
        self.place = Place()
        self.city = City()
        self.user = User()
        self.amenity = Amenity()

    def tearDown(self):
        ''' Tear down '''
        del self.place
        del self.user

    def test_place_creation(self):
        ''' Tests if Place is created and all elements are initialised
            properly '''

        self.assertIsInstance(self.place, Place)
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_place_assignment(self):
        ''' Tests if things are assigned properly '''

        self.place.city_id = self.city.id
        self.place.user_id = self.user.id
        self.place.name = "Ethiopia"
        self.place.description = "The best place on Earth"
        self.place.number_rooms = 10
        self.place.number_bathrooms = 4
        self.place.max_guest = 3
        self.place.price_by_night = 50
        self.place.latitude = 34.0
        self.place.longitude = 33.7
        self.place.amenity_ids.append(self.amenity.id)

        self.assertEqual(self.place.city_id, self.city.id)
        self.assertEqual(self.place.user_id, self.user.id)
        self.assertEqual(self.place.name, "Ethiopia")
        self.assertEqual(self.place.description, "The best place on Earth")
        self.assertEqual(self.place.number_rooms, 10)
        self.assertEqual(self.place.number_bathrooms, 4)
        self.assertEqual(self.place.max_guest, 3)
        self.assertEqual(self.place.price_by_night, 50)
        self.assertEqual(self.place.latitude, 34.0)
        self.assertEqual(self.place.longitude, 33.7)
        self.assertEqual(self.place.amenity_ids, [self.amenity.id])


if __name__ == "__main__":
    unittest.main()
