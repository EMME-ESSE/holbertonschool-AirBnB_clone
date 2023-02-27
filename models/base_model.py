#!/usr/bin/python3
"""
class base models

"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Class"""
    def __init__(self):
        """Constructor that assigns a unique id using"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
    def __str__(self):
        """Returns a string representation of the instance"""
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.new(self)

    def to_dict(self):
        """Returns a dictionary containing all instance attributes"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = type(self).__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy

    def __init__(self, *args, **kwargs):
        """Generate a dictionary representation of an instance"""
        if kwargs:
            kwargs.pop('__class__', None)
            self.__dict__.update(kwargs)
            self.created_at = datetime.strptime(self.created_at,'%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(self.updated_at,'%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
