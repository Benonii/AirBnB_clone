#!/usr/bin/python3

''' Takes care of string and retrieving all changes, presistnece. '''

import os
import json
from models.base_model import BaseModel


class FileStorage:
    ''' This class stores all created objects into a file and restores them.
        <class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump ->
        <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'>
        -> <class 'BaseModel'>
    '''

    def __init__(self):
        ''' Instantization '''
        self.__file_path = "file.jsom"
        self.__objects = {}

    def all(self):
        ''' Prints sll elements of the private attr objects '''
        self.__objects

    def new(self, obj):
        ''' Sets in __objects the obj with key <obj class name>.id '''
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        ''' Saves objects into a file specified by __file_path. '''

        filename = self.__file_path
        list_dicts = []

        with open(filename, "a", encoding="utf-8") as f:
            for obj in self.__objects:
                dict_rep = obj.to_dict()
                list_dicts.append(dict_rep)

            if list_dicts is not None:
                json_str = json.dumps(list_dicts)
            f.write(json_str)

    def reload(self):
        ''' deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists; otherwise, do nothing)
        '''

        filename = self.__file_path
        
        if os.path.exists(filename):
            with open(filename ,"r", encoding="utf-8") as f:
                list_of_dicts = json.loads(f.read())

            for dict in list_of_dicts:
                instance = basemodel.BaseModel(**dict)
                self.new(obj)
        else:
            pass
