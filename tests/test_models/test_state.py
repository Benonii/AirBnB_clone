#!/usr/bin/python3

''' This module contains unit tests for the class State '''

import unittest
from models.base_model import BaseModel
from models.state import State


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


if __name__ == "__main__":
    unittest.main()
