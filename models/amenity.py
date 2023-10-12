#!/usr/bin/python3

''' This module contains the class Amenity. '''

from models.base_model import BaseModel


class Amenity(BaseModel):
    ''' This class inherits from BaseModel. '''

    def __init__(self):
        ''' Instantisation '''
        self.name = ""
        super().__init__()
