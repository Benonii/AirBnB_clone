#!/usr/bin/python3

''' A module containing the class User. '''

from models.base_model import BaseModel


class User(BaseModel):
    ''' A class that inherits from BaseModel '''

    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""

    def __init__(self, *args, **kwargs):
        ''' Instantization '''
        super().__init__(*args, **kwargs)
