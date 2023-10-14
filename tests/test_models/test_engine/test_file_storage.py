import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        ''' Set up '''
        self.storage = FileStorage()

    def tearDown(self):
        ''' Tear down '''
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_attribute_creation(self):
        ''' Tests if the attributes are created and initialized properly '''
        self.assertIsInstance(self.storage._FileStorage__file_path, str)
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all_empty(self):
        ''' Tests the method `all` when it's empty '''
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(len(all_objects), 0)

    def test_new(self):
        ''' Tests the method `new` when it's empty '''
        obj = BaseModel()
        self.storage.new(obj)
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertIn(f"BaseModel.{obj.id}", all_objects)

    def test_save_base_model(self):
        ''' Tests the method `save` for base model '''
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as f:
            data = f.read()
        self.assertIn(f"BaseModel.{obj.id}", data)

    def test_reload_exists(self):
        ''' Tests the method `reload` for base_model '''
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        self.assertEqual(len(all_objects), 1)

if __name__ == '__main__':
    unittest.main()

