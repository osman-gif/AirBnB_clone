#!/usr/bin/python3
"""
This module provide command interpreter AKA the console program,
from which you can control the AirBNB project: create and destroy an
object and so on
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class inherits the Cmd class from the cmd module,
    The class 'HBNBCommand' is used for managing the objects of the AirBnb
    project
    """

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """ Quit command to exit the program """

        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        return True

    def do_create(self, class_name):
        """ Create an object of the class_name class """
        obj = None
        if class_name:
            match(class_name):
                case "BaseModel":
                    obj = BaseModel()
                case _:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")
            return True
        if obj is not None:
            obj.save()
            id = "{}".format(obj.id)
            print(id)
        else:
            return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
