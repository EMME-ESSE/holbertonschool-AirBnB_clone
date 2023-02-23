#!/usr/bin/python3
"""


"""
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

    def all(self):
        """ return dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        FileStorage.__objects['{}.{}']

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """

    def reload(self):
