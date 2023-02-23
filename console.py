#!/usr/bin/python3
"""
console AirBnB project

"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

import cmd


class HBNBCommand(cmd.Cmd):
    """
    clone console AirBnB

    """
    prompt = '(hbnb) '

    def EOF(self, args):
        """ end of file """
        return True

    def quit(self, args):
        """ quit program """
        return True

    def emptyLine(self):
        """ empty line """
        pass

if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()
