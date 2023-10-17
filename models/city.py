#!/usr/bin/python3

''' This module contains the class City. '''

from models.base_model import BaseModel


class City(BaseModel):
    ''' This class inherits from BaseModel. '''

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        ''' Instantisation. '''
        super().__init__(*args, **kwargs)
