#!/usr/bin/python3
"""
This module provide command interpreter AKA the console program,
from which you can control the AirBNB project: create and destroy an
object and so on
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """The HBNBCommand class inherits the Cmd class from the cmd module,
    The class 'HBNBCommand' is used for managing the objects of the AirBnb
    project
    """

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program
        """

        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program
        """

        print()
        return True

    def emptyline(self):
        """Called when an empty line is entered"""

        print(end="")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
