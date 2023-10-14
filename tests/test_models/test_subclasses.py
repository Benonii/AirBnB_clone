#!/usr/bin/python3

''' This module contains unittests for the subclasses User, State, City
    Amenity, Place and Review. '''

import unittest
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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


class TestState(unittest.TestCase):
    ''' Tests the class State '''

    def setUp(self):
        ''' Set up '''
        self.state = State()

    def tearDown(self):
        ''' Tear down '''
        del self.state

    def test_state_creation(self):
        ''' Tests if state is created and all elements are initialised properly
        '''

        self.assertIsInstance(self.state, State)
        self.assertEqual(self.state.name, "")

    def test_state_assignment(self):
        ''' Tests if name is assigned correctly '''

        self.state.name = "Dakota"

        self.assertEqual(self.state.name, "Dakota")


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


class TestReview(unittest.TestCase):
    ''' Tests the class Review '''

    def setUp(self):
        ''' Set up '''
        self.review = Review()
        self.place = Place()
        self.user = User()

    def tearDown(self):
        ''' Tear down '''
        del self.review
        del self.place
        del self.user

    def test_review_creation(self):
        ''' Tests if Review is created and all elements are initialised
            properly '''

        self.assertIsInstance(self.review, Review)
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_review_assignment(self):
        ''' Tests if everything is assigned properly '''

        self.review.place_id = self.place.id
        self.review.user_id = self.user.id
        self.review.text = "Great place"

        self.assertEqual(self.review.place_id, self.place.id)
        self.assertEqual(self.review.user_id, self.user.id)
        self.assertEqual(self.review.text, "Great place")


if __name__ == "__main__":
    unittest.main()
