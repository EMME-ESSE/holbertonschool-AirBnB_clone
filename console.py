#!/usr/bin/python3
"""
console AirBnB project

"""

# import models
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

    if __name__ == '__main__':
        console = HBNBCommand()
        console.cmdloop()


# hasta acá es lo que hice hace unos días viendo ejercicios.
