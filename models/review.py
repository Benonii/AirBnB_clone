#!/usr/bin/python3

''' This module contains the class Review. '''

from models.base_model import BaseModel


class Review(BaseModel):
    ''' This class inherits from the base class BaseModel. '''

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        ''' Instantisation. '''
        super().__init__(*args, **kwargs)
