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
        self.__clas__.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, 'w+') as f:
            new_dictionary = {}
            for key, value in self.__class__.__objects.items():
                new_dictionary[key] = value.to_dict()
                json.dump(new_dictionary, f)    

    def reload(self):
        """Crea una lista de una sola tupla  (class_name, obj_id) a partir de la cadena key usando el método split para despues 
        separarlas con formato {class_name}.{obj_id}
        Primer for: comprensión de diccionario.
        Segundo for: itera a través de todos los elementos del diccionario new_dictionary,
        Cada llave es una cadena con el formato "<class_name>.<obj_id>", class_name es el nombre de la clase del objeto y obj_id es el 
        identificador único del objeto.
        
        Crea una nueva instancia de la clase y agrega al diccionario __objects utilizando la llave f"{class_name}.{obj_id}". 
        Si el archivo JSON no existe, se omite la excepción y el diccionario __objects permanece vacío."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                new_dictionary = json.load(f)
                FileStorage.__objects = {f"{class_name}.{obj_id}": eval(class_name)(**value) 
                                        for key, value in new_dictionary.items()
                                        for class_name, obj_id in [key.split('.')] }
        except FileNotFoundError:
            pass
