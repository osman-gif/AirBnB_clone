#!/usr/bin/python3
"""
This module provide command interpreter AKA the console program,
from which you can control the AirBNB project: create and destroy an
object and so on
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """The HBNBCommand class inherits the Cmd class from the cmd module,
    The class 'HBNBCommand' is used for managing the myobjects of the AirBnb
    project
    """
    def class_exist(self, class_name):
        """checks if a class exists"""
        match(class_name):
            case "BaseModel":
                return 'yes'
            case _:
                return 'no'

    def instance_exist(self, class_name, id):
        """Checks if an instance exists"""

        result = self.class_exist(class_name)
        if result == 'yes':
            if f"{class_name}.{id}" in FileStorage().all().keys():
                return 'yes'
            else:
                return 'no'

    def attribute_exist(self, class_name, id, attribute):
        """Checks if an attributes exists"""

        result = self.instance_exist(class_name, id)
        if result == 'yes':
            if attribute in FileStorage(
                
            ).all()[f"{class_name}.{id}"].to_dict().values():
                return 'yes'
            else:
                return 'no'
        return 'no'

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

    def do_create(self, class_name):
        """Create an object of the class_name class
        """

        obj = None
        if class_name:
            match(class_name):
                case "BaseModel":
                    obj = BaseModel()
                case _:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")
            self.emptyline()
        if obj is not None:
            obj.save()
            id = "{}".format(obj.id)
            print(id)
        else:
            self.emptyline()

    def do_show(self, line):
        """Prints the string representation
        of an instance based on the class name and id
        """

        args = line.split()
        class_name = args[0]
        obj_id = args[1]

        cls = None

        if class_name:

            match class_name:
                case "BaseModel":
                    cls = BaseModel()
                case _:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

        if obj_id:
            myobjects = FileStorage().all()
            if f"{class_name}.{obj_id}" in myobjects.keys():
                print(myobjects[f"{class_name}.{obj_id}"])
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_destroy(self, line):
        """Deletes an instance"""

        args = line.split()
        class_name = args[0]
        obj_id = args[1]

        cls = None

        if class_name:
            match class_name:
                case "BaseModel":
                    cls = BaseModel()
                case _:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

        if obj_id:
            myobjects = storage.all()

            if f"{class_name}.{obj_id}" in myobjects.keys():
                del storage.all()[f"{class_name}.{obj_id}"]
                FileStorage().save()
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_all(self, class_name):
        """Prints all string representation of all
        instances based or not on the class name"""

        objs_list = []
        cls = None

        if class_name:
            match class_name:
                case 'BaseModel':
                    all_obj = storage.all()
                    for value in all_obj.values():
                        objs_list.append(str(value))
                    print(objs_list)
                case _:
                    print("** class doesn't exist **")
        else:
            print(storage.all())

    def do_update(self, line):
        """Updates an instance based on the class
        name and id by adding or updating attribute"""

        # extract arguments
        args = line.split()
        args_len = len(args)

        if args_len == 4:
            class_name = args[0]
            id = args[1]
            attribute = args[2]
            attr_value = args[3]

            cls_exist = self.class_exist(class_name)
            inst_exist = self.instance_exist(class_name, id)
            attribute_exist = self.attribute_exist(class_name, id, attribute)

            instance = storage.all()[f"{class_name}.{id}"].to_dict()

            match type(attribute):
                case str():
                    attr_value = str(attr_value)
                case float():
                    attr_value = float(attr_value)
                case int():
                    attr_value = int(attr_value)
                case _:
                    pass

            instance[attribute] = attr_value
            FileStorage().save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
