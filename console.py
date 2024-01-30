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

    def do_create(self, class_name):
        """Create an object of the class_name class
        """
        classes = {"Amenity": Amenity(), "User": User(), "State": State(),
                   "BaseModel": BaseModel(), "Place": Place(), "City": City(),
                   "Review": Review()}
        obj = None
        if class_name:
            if class_name in classes.keys():
                for key, value in classes.items():
                    if class_name == key:
                        obj = value
            else:
                print("** class doesn't exist **")
                return
        else:
            print("** class name missing **")
            return
        if obj is not None:
            obj.save()
            id = "{}".format(obj.id)
            print(id)
        else:
            self.emptyline()

    def instance_exist(self, class_name, obj_id):
        """Checks if an instance exists"""

        _class = oxilury_file.class_exist(class_name)
        _instance = oxilury_file.instance_exist(class_name, obj_id)
        if _class == "yes":
            pass
        else:
            print("** class does not exist  **")
            return
        if _instance == "yes":
            pass
        else:
            print("instance does not exist")
            return

        return storage.all()[f"{class_name}.{obj_id}"]

    def do_show(self, line):
        """Prints the string representation
        of an instance based on the class name and id
        """

        class_name = None
        obj_id = None

        args = line.split()
        args_len = len(args)

        if args_len == 0:
            print("** class name is missing")
            return
        if args_len <= 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        obj_id = args[1]

        obj = self.instance_exist(class_name, obj_id)
        if obj:
            print(obj)

    def do_destroy(self, line):
        """Deletes an instance"""

        class_name = None
        obj_id = None

        args = line.split()
        args_len = len(args)

        if args_len == 0:
            print("** class name is missing")
            return
        if args_len <= 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        obj_id = args[1]

        obj = self.instance_exist(class_name, obj_id)
        if obj:
            del FileStorage().all()[f"{class_name}.{obj_id}"]

    def do_all(self, class_name):
        """Prints all string representation of all
        instances based or not on the class name"""

        classes = ['BaseModel', 'City', 'Amenity', 'State',
                   'User', 'Review', 'Place']
        objs_list = []

        if class_name:
            if class_name in classes:
                all_obj = storage.all()
                for key, value in all_obj.items():
                    if class_name in key:
                        objs_list.append(str(value))
                print(objs_list)
            else:
                print("** class doesn't exist **")
                return
        else:
            all_obj = []
            for key, value in storage.all().items():
                all_obj.append(str(storage.all()[key]))
            print(all_obj)

    def do_update(self, line):

        """Updates an instance based on the class
        name and id by adding or updating attribute"""

        class_name = None
        id = None
        attribute = None
        attr_value = None

        # extract arguments
        args = line.split()
        args_len = len(args)

        if args_len == 0:
            print("** class name missing **")
            return
        elif args_len == 1:
            print("** instance id missing **")
            return
        elif args_len == 2:
            print("** attribute name missing **")
            return
        elif args_len == 3:
            print("** value missing **")
            return
        elif args_len >= 4:
            class_name = args[0]
            id = args[1]
            attribute = args[2]
            attr_value = args[3]

        cls_exist = oxilury_file.class_exist(class_name)
        inst_exist = oxilury_file.instance_exist(class_name, id)
        attr_exist = oxilury_file.attribute_exist(class_name, id, attribute)

        if cls_exist == 'yes':
            if inst_exist == 'yes':

                instance = storage.all()[f"{class_name}.{id}"]

                match type(attribute):
                    case str():
                        attr_value = str(attr_value)
                    case float():
                        attr_value = float(attr_value)
                    case int():
                        attr_value = int(attr_value)
                    case _:
                        pass
                f = f"{attribute}"
                print(f)
                setattr(instance, attribute, attr_value)
                # instance.(f{"attibute"}) = attr_value
                instance.save()

            else:
                print("** no instance found **")
                return
        else:
            print("** class doesn't exist **")
            return

    def default(self, line: str) -> None:
        """
        This function execute other commands
        """
        class_name, command = line.split('.')

        oxilury_file.execute_default_command(class_name, command)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
