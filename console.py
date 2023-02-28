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
    
    def valid(self, args):
        if not args.strip():
            return False
        else:
            return True




    def do_EOF(self, args):
        """ exit with Ctrl + D """
        return True

    def do_quit(self, args):
        """ quit program """
        return True

    def emptyLine(self):
        """ empty line """
        pass

    def do_create(self, args):
        """ create a new instance """
        token = args.split()

        if len(args) == 0:
            print('** class name missing **')
            return
        elif token[0] not in HBNBCommand().classes:
            print("** class doesn't exist **")

        try:
            new_instance = eval(token[0])()
            new_instance.save()
            print(new_instance.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ prints string of an instance on the class name and id """
        token = args.split()

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

    def do_destroy(self, args):
        """ delete an instances """
        token = args.split()

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

    def do_all(self, args):
        """ prints string of all instances based or not on the class name """
        token = args.split()

        if len(token) == 0:
            print([str(value) for key, value in storage.all().items()])
        elif token[0] not in HBNBCommand().classes:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in storage.all().items()
                   if value.__class__.__name__ == token[0]])

    def do_update(self, args):
        """ updates instance on the class name and id """
        token = args.split()

        if len(token) == 0:
            print('** class name missing **')
        elif token[0] not in HBNBCommand().classes:
            print("** class doesn't exist **")
        elif len(token) == 1:
            print('** instance id missing **')
        else:
            for key, value in storage.all().items():
                if (value.__class__.__name__ == token[0] and
                        value.id == token[1].strip('"')):
                    if len(token) == 2:
                        print('** attribute name missing **')
                    elif len(token) == 3:
                        print('** value missing **')
                    else:
                        setattr(value, token[2], token[3])
                        storage.save()
            key = '{}.{}'.format(token[0], token[1])
            if key not in storage.all().keys():
                print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
