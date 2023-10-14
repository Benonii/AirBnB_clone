#!/usr/bin/python3

''' This module contains the base model that all other classes inherit from '''

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    ''' Base class '''

    def __init__(self, *args, **kwargs):
        ''' instantization '''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs is not None:
            class_name = kwargs.pop("__class__", None)
            
            if class_name:
                # Dynamically load the class based on the class name
                class_ref = globals().get(class_name)
                
                if class_ref:
                    self.__class__ = class_ref

            for key, value in kwargs.items():

                # Convert string to dattime module for these two attributes
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "id":
                    value = str(value)

                # Set attributes
                setattr(self, key, value)
        storage.new(self)

    def __str__(self):
        ''' returns a printable string of the object '''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        ''' Updates the public instance attribute `updated_at with the cuurent
            datetime. '''

        # Saves all current objects to a json file
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' returns a dictionary containing all keys, values of __dict__ of the
            instance. '''

        Dict = {}
        for key, value in self.__dict__.items():
            if value is not None:

                # Covnvert string to datetime module for these two attributes
                if key == "created_at" or key == "updated_at":
                    Dict[key] = datetime.isoformat(value)
                else:
                    Dict[key] = value
        Dict["__class__"] = 'BaseModel'
        return Dict
