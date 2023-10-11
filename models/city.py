#!/usr/bin/python3

''' This module contains the class City. '''

from models.base_model import BaseModel


class City(BaseModel):
    ''' This class inherits from BaseModel. '''

    def __init__(self):
        ''' Instantisation. '''
        self.state_id = ""
        self.name = ""
        super().__init__()
