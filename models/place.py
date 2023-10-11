#!/usr/bin/python3

''' This module contains the class Place. '''

from models.base_model import BaseModel


class Place(BaseModel):
    ''' This class inherits from the base class BaseModel. '''

    def __init__(self):
        ''' Instantisation '''
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self. description = ""
        self.number_room = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        super.__init__()
