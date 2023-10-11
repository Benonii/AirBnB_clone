#!/usr/bin/python3

''' A module containing the class User. '''

from models.base_model import BaseModel

class User(BaseModel):
    ''' A class that inherits from BaseModel '''

    def __init__(self):
        ''' Instantization '''
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

        super().__init__()
