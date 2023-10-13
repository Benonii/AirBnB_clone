#!/usr/bin/python3

''' THis module contains the class State. '''

from models.base_model import BaseModel


class State(BaseModel):
    ''' This class inherits from the base class BaseModel. '''

    def __init__(self, *args, **kwargs):
        ''' Instantization '''
        self.name = ""

        super().__init__(*args, **kwargs)
