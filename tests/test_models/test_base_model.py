#!/usr/bin/python3
'''a module to test the base model'''


import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBase_init(unittest.TestCase):
    '''a class to test the base module'''

    def test_objectCreated(self):
        '''test that the object was created and its type is BaseModel'''

        m = BaseModel()
        self.assertEqual(BaseModel, type(m))

    def test_objectStored(self):
        '''test that the object that was created is stored inside the storage
        '''

        m = BaseModel()
        self.assertIn(m, models.storage.all().values())

    def test_objectIdIsStr(self):
        '''checks if the id was created as a string'''

        m = BaseModel()
        self.assertEqual(type(m.id), str)

    def test_objectCreated_atIsDatetime(self):
        '''checks if the created_at was created as a datetime'''

        m = BaseModel()
        self.assertEqual(type(m.created_at), datetime)

    def test_objectCreated_atISDiff(self):
        '''checks if the object is created at different times'''

        m = BaseModel()
        sleep(1)
        n = BaseModel()
        self.assertNotEqual(m.created_at, n.created_at)

    def test_objectUpdated_atIsDatetime(self):
        '''checks if the updated_at was created as a datetime'''

        m = BaseModel()
        self.assertEqual(type(m.updated_at), datetime)

    def test_objectUpdated_atIsDiff(self):
        '''checks if the object is updated at different times'''

        m = BaseModel()
        sleep(1)
        n = BaseModel()
        self.assertNotEqual(m.updated_at, n.updated_at)

    def test_objectIdIsUnique(self):
        '''checks if the id was created differently
        from instance to another
        '''

        m = BaseModel()
        n = BaseModel()
        self.assertNotEqual(m.id, n.id)


class TestBase_str(unittest.TestCase):
    '''a class to test the str function'''

    def test_strIsStr(self):
        '''checks if the str function prints a string'''

        m = BaseModel()
        self.assertEqual(str, type(m.__str__()))

    def test_rightPrint(self):
        '''checks if the str function prints the right string'''

        m = BaseModel()
        s = "[{}] ({}) {}".format(m.__class__.__name__, m.id,
                                  m.__dict__)
        self.assertEqual(s, m.__str__())


class TestBase_save(unittest.TestCase):
    '''a class to test the save function'''

    def test_isUpdated(self):
        '''checks if the time was changed when save & it is the right time'''

        m = BaseModel()
        time = m.updated_at
        sleep(1)
        m.save()
        time2 = m.updated_at
        self.assertNotEqual(time, time2)


class TestBase_dict(unittest.TestCase):
    '''a class to test the to_dict function'''

    def test_isAttributeThere(self):
        '''checks if the directory have all of the attributes of the class'''

        m = BaseModel()
        self.assertIn("id", m.to_dict())
        self.assertIn("created_at", m.to_dict())
        self.assertIn("updated_at", m.to_dict())
        self.assertIn("__class__", m.to_dict())

    def test_canAddAttributes(self):
        '''checks if the directory have the new created attributes'''

        m = BaseModel()
        m.first_name = "Jack"
        m.last_name = "Will"
        m.number = 28
        self.assertIn("first_name", m.to_dict())
        self.assertIn("last_name", m.to_dict())
        self.assertIn("number", m.to_dict())

    def test_isRightValues(self):
        '''checks if the directory have the right values'''

        m = BaseModel()
        m.first_name = "Jack"
        m.last_name = "Will"
        m.number = 28
        self.assertEqual("Jack", m.to_dict()["first_name"])
        self.assertEqual("Will", m.to_dict()["last_name"])
        self.assertEqual(28, m.to_dict()["number"])

    def test_dictIsDict(self):
        '''checks if the dict's return value's type is dict'''

        m = BaseModel()
        self.assertEqual(dict, type(m.to_dict()))

    def test_classIsTheNameOfTheClass(self):
        '''checks if the __class__ has the name of the object'''

        m = BaseModel()
        self.assertEqual("BaseModel", m.to_dict()["__class__"])

    def test_rightReturn(self):
        '''checks if the to_dict function returns the correct answer'''

        m = BaseModel()
        time = m.created_at
        m.id = "28"
        sleep(1)
        m.save()
        m.created_at = time
        m.updated_at = time
        time = time.isoformat()
        dictionary = {
                'id': '28',
                '__class__': 'BaseModel',
                'created_at': time,
                'updated_at': time,
            }
        self.assertEqual(dictionary, m.to_dict())


if __name__ == "__main__":
    unittest.main()
