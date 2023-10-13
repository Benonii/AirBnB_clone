#!/usr/bin/python3
'''a module to test the base model'''


import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBase_inti(unittest.TestCase):
    '''a class to test the base module'''

    def test_objectCreated(self):
        '''test that the object was created and its type is BaseModel'''
        
        m = BaseModel()
        self.assertEqual(BaseModel, type(m))

    def test_objectStored(self):
        '''test that the object that was created is stored inside the storage'''

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
    '''a class to test the dict function'''

    pass

if __name__ == "__main__":
    unittest.main()
