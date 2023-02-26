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
        """ exit with Ctrl + D """
        return True

    def quit(self, args):
        """ quit program """
        return True

    def emptyLine(self):
        """ empty line """
        pass

    def create(self, args):
        """ create a new instance """
        if len(args) == 0:
            print('** class name missing **')
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance = save()
            prints(instance.id)



if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()
