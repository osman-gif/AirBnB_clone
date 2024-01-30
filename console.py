#!/usr/bin/python3
"""
This module provide command interpreter AKA the console program,
from which you can control the AirBNB project: create and destroy an
object and so on
"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models.state import State
from models.__init__ import storage
import oxilury_file


class HBNBCommand(cmd.Cmd):
    """The HBNBCommand class inherits the Cmd class from the cmd module,
    The class 'HBNBCommand' is used for managing the myobjects of the AirBnb
    project
    """

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program
        """

        return 1

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
