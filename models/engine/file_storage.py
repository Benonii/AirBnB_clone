#!/usr/bin/python3

''' Takes care of string and retrieving all changes, presistnece. '''


import json


class FileStorage:
    ''' This class stores all created objects into a file and restores them.
        <class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump ->
        <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'>
        -> <class 'BaseModel'>
    '''

    def __init__(self):
        ''' Instantization '''
        self.__file_path = "file.json"
        self.__objects = dict()

    def all(self):
        ''' Prints sll elements of the private attr objects '''
        return self.__objects

    def new(self, obj):
        ''' Sets in __objects the obj with key <obj class name>.id '''
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        ''' Saves objects into a file specified by __file_path. '''

        filename = self.__file_path
        data_to_write = {}

        for key, obj in self.__objects.items():
            data_to_write[key] = obj.to_dict()

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data_to_write, f)

    def reload(self):
        ''' deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists; otherwise, do nothing)
        '''
        
        # Putting this import statement in the beginning was causing issues.
        from models.base_model import BaseModel

        filename = self.__file_path

        try:
            with open(filename, "r", encoding="utf-8") as f:
                list_of_dicts = json.loads(f.read())

            for key, value in list_of_dicts.items():
                class_name, obj_id = key.split(".")
                instance = BaseModel(**value)
                self.__objects[key] = instance

        except FileNotFoundError:
            pass
