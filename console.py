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
    classes = {'BaseModel',
               'Amenity',
               'City',
               'Place',
               'Review',
               'State',
               'User'}

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
        token = parse(args)

        if len(token) == 0:
            print('** class name missing **')
        elif token[0] not in HBNBCommand().classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance = save()
            prints(instance.id)

    def show(self, args):
        """ prints string of an instance on the class name and id """
        token = parse(args)

        if len(token) == 0:
            print('** class name missing **')
        elif token[0] not in HBNBCommand().classes:
            print("** class doesn't exist **")
        elif len(token) == 1:
            print('** instance id missing **')
        else:
            key = '{}.{}'.format(token[0], token[1])
            if key not in storage.all().keys():
                print('** no instance found **')
            else:
                print(storage.all()[key])

    def destroy(self, args):
        """ delete an instances """
        token = parse(args)

        if len(token) == 0:
            print('** class name missing **')
        elif token[0] not in HBNBCommand().classes:
            print("** class doesn't exist **")
        elif len(token) == 1:
            print('** instance id missing **')
        else:
            key = '{}.{}'.format(token[0], token[1])
            if key not in storage.all().keys():
                print('** no instance found **')
            else:
                del storage.all()[key]
                storage.save()

if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()
