#!/usr/bin/python3

''' This module contains the class Review. '''

from models.base_model import BaseModel


class Review(BaseModel):
    ''' This class inherits from the base class BaseModel. '''

    def __init__(self, *args, **kwargs):
        ''' Instantisation. '''
        self.place_id = ""
        self.user_id = ""
        self.text = ""

        super().__init__(*args, **kwargs)
