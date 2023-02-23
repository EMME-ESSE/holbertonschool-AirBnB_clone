import uuid
from datetime import datetime
import models

class BaseModel:
    """Class"""
    def __init__(self):
        """Constructor that assigns a unique id using"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

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
            for key, value in kwargs.items():
                if key == '__class__':
                    continue

                #esto no se como pasarl oa tiempo real, me fije el comando strptime pero no entendi la consigna
                # y no se si tengo que ponter algo como self.update_at = datetime.strptime(self.update_at, "%Y-%m-%dT%H:%M:%S.%f") 
                #porque no se si lo que tiene que modificarse es eso o hacer otra variable nueva
                if key == 'created_at' or key == 'update_at'
                    dateTime = '%Y-%m-%dT %H:%M:%S.%f'
                    value = datetime.strptime(kwargs[key], dateTime)

                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
