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
        key = '{}.{}'.format(obj.__clas__.__name__, str(obj.id))
        self.__clas__.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, 'w+') as f:
            new_dictionary = {}
            for key, value in self.__clas__.__objects__.items():
                new_dictionary[key] = value.to_dict()
                f.write(json.dumps(new_dictionary))

    def reload(self):
        """  deserializes the JSON file to __objects """
        #deserializes the JSON file to __objects (only if the JSON file (__file_path) exists

        #otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
