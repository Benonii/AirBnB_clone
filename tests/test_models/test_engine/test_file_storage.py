#!/usr/bin/python3

''' This module contains tests for the class FileStorage. '''

import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up the test environment."""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after the tests."""
        self.storage._FileStorage__objects = {}
        try:
            with open(self.storage._FileStorage__file_path, "w") as f:
                f.write(json.dumps({}))
        except FileNotFoundError:
            pass

    def test_instance_attributes(self):
        """Test if FileStorage has the expected instance attributes."""
        self.assertTrue(hasattr(self.storage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(self.storage, '_FileStorage__objects'))

        self.assertIsInstance(self.storage._FileStorage__file_path, str)
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all_method_empty(self):
        """Test the all() method."""
        self.assertIsInstance(self.storage.all(), dict)
        self.assertEqual(len(self.storage.all()), 0)

    def test_new_method(self):
        """Test the new() method."""
        new_model = BaseModel()
        self.storage.new(new_model)
        self.assertTrue("BaseModel." + new_model.id in
                        self.storage._FileStorage__objects)

    def test_all_method_not_empty(self):
        """ Tests the all() method when it's not empty """
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(len(self.storage.all()), 1)

    def test_save_method(self):
        """Test the save() method."""
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as f:
            data = json.load(f)
        self.assertIn("BaseModel." + new_model.id, data)

    def test_reload_method(self):
        """Test the reload() method."""
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()
        self.storage.reload()
        self.assertTrue("BaseModel." + new_model.id in self.storage.all())

    def test_all_subclasses(self):
        ''' Tests the methods all(), new(), save() and reload() for subclasses.
        '''
        new_user = User()
        new_state = State()
        new_city = City()
        new_amenity = Amenity()
        new_place = Place()
        new_review = Review()

        self.storage.new(new_user)
        self.storage.new(new_state)
        self.storage.new(new_city)
        self.storage.new(new_place)
        self.storage.new(new_amenity)
        self.storage.new(new_review)

        self.assertEqual(len(self.storage.all()), 6)

        self.storage.save()
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 6)


class TestModels(unittest.TestCase):
    """Test cases for the models linked to FileStorage."""

    def setUp(self):
        """Set up the test environment."""
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """Clean up after the tests."""
        self.storage._FileStorage__objects = {}
        try:
            with open(self.storage._FileStorage__file_path, "w") as f:
                f.write(json.dumps({}))
        except FileNotFoundError:
            pass

    def test_base_model_link_to_storage(self):
        """Test linking BaseModel objects to FileStorage."""
        new_model = BaseModel()

        self.storage.new(new_model)
        self.assertTrue("BaseModel." + new_model.id in self.storage.all())

    def test_user_link_to_storage(self):
        """Test linking User objects to FileStorage."""
        new_user = User()

        self.storage.new(new_user)
        self.assertTrue("User." + new_user.id in self.storage.all())

    def test_state_link_to_storage(self):
        """Test linking State objects to FileStorage."""
        new_state = State()

        self.storage.new(new_state)
        self.assertTrue("State." + new_state.id in self.storage.all())

    def test_city_link_to_storage(self):
        """Test linking City objects to FileStorage."""
        new_city = City()

        self.storage.new(new_city)
        self.assertTrue("City." + new_city.id in self.storage.all())

    def test_amenity_link_to_storage(self):
        """Test linking Amenity objects to FileStorage."""
        new_amenity = Amenity()

        self.storage.new(new_amenity)
        self.assertTrue("Amenity." + new_amenity.id in self.storage.all())

    def test_place_link_to_storage(self):
        """Test linking Place objects to FileStorage."""
        new_place = Place()

        self.storage.new(new_place)
        self.assertTrue("Place." + new_place.id in self.storage.all())

    def test_review_link_to_storage(self):
        """Test linking Review objects to FileStorage."""
        new_review = Review()

        self.storage.new(new_review)
        self.assertTrue("Review." + new_review.id in self.storage.all())


if __name__ == '__main__':
    unittest.main()
