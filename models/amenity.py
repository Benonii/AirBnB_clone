#!/usr/bin/python3

''' This module contains the class Amenity. '''

from models.base_model import BaseModel


class Amenity(BaseModel):
    ''' This class inherits from BaseModel. '''

    name = ""

    def __init__(self, *args, **kwargs):
        ''' Instantisation '''

        super().__init__(*args, **kwargs)
