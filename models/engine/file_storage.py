#!/usr/bin/python3
"""Storage"""


import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """ serializes and deserializes JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = '{}.{}'.format(obj.__class__.__name__, str(obj.id))
        self.__class__.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            new_dictionary = {}
            for key, value in self.__objects.items():
                new_dictionary[key] = value.to_dict()
                json.dump(new_dictionary, f)

    def reload(self):
        """Function reload"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                new_dictionary = json.load(f)
                for key, value in new_dictionary.items():
                    obj_class = value['__class__']
                    obj_instance = eval(obj_class + "(**value)")
                    FileStorage.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
