#!/usr/bin/python3
"""Storage"""


from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

import json


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
        with open(FileStorage.__file_path, 'w+') as f:
            new_dictionary = {}
            for key, value in self.__class__.__objects.items():
                new_dictionary[key] = value.to_dict()
                json.dump(new_dictionary, f)    
    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                new_dictionary = json.load(f)
                FileStorage.__objects = {}
            for key, value in new_dictionary.items():
                class_name, obj_id = key.split('.')
                obj_instance = eval(class_name)(**value)
                obj_key = f"{class_name}.{obj_id}"
                FileStorage.__objects[obj_key] = obj_instance
        except FileNotFoundError:
            pass
