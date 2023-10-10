#!/usr/bin/python3

''' This module contains the base model that all other classes inherit from '''

import uuid
from datetime import datetime


class BaseModel:
    ''' Base class '''

    def __init__(self, *args, **kwargs):
        ''' instantization '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

    def __str__(self):
        ''' returns a printable string of the object '''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        ''' Updates the public instance attribute `updated_at with the cuurent
            datetime. '''

        self.updated_at = datetime.now()

    def to_dict(self):
        ''' returns a dictionary containing all keys, values of __dict__ of the
            instance. '''
        
        Dict = {}
        for key, value in self.__dict__.items():
            if value is not None:
                if key == "created_at" or key == "updated_at":
                    Dict[key] = datetime.isoformat(value)
                else:
                    Dict[key] = value
        return Dict
