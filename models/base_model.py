#!/usr/bin/python3
"""
class base models

"""
import uuid
import datetime
import models


class BaseModel:
    """Class"""
    def __init__(self):
        """Constructor that assigns a unique id using"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
    
    def __str__(self):
        """Returns a string representation of the instance"""
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        BaseModel.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all instance attributes"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
    
    def __init__(self, *args, **kwargs):
        """Generate a dictionary representation of an instance"""
        if kwargs is not None and len(kwargs) != 0:
             for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)