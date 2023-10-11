#!/usr/bin/python3

''' THis module contains the class State. '''

from models.base import BaseModel


class State(BaseModel):
    ''' This class inherits from the base class BaseModel. '''

    def __init__(self):
        ''' Instantization '''
        self.name = ""
        super.__init__()
