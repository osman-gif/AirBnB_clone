#!/usr/bin/python3

""" This is oxilary file or helper file """
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import console


def execute_default_command(class_name, command):
    """
    This function execute default commands
    """
    classes = [
         "BaseModel", "User", "State", "Place", "City", "Amenity", "Review"]
    commands = {"all": "all()", "count": "Count()"}

    if class_name in classes:
        if command == "all()":
            console.HBNBCommand.do_all(class_name)
        elif command == "count()":
            print(FileStorage().all_class_count(class_name))
        elif "show" in command:
            for key in FileStorage().all().keys():
                if key.split('.')[1] == command.split("\"")[1]:
                    print(FileStorage().all()[key])
                    return
            print("** no instance found **")

        elif "destroy" in command:
            id = 0
            for key in FileStorage().all().keys():
                if key.split('.')[1] == command.split("\"")[1]:
                    print(command.split("\""))
                    id = key.split('.')[1]

            if id != 0:
                FileStorage().destroy(id)
                BaseModel().save()
                return
            print("** no instacne found **")
    else:
        print("** class does not exist **")
        return

    return


def class_exist(class_name):
    """checks if a class exists, if so then return 'yes'
    else 'no' """

    match class_name:
        case "BaseModel":
            return 'yes'
        case "User":
            return 'yes'
        case "State":
            return 'yes'
        case "City":
            return 'yes'
        case "Review":
            return 'yes'
        case "Amenity":
            return 'yes'
        case _:
            return 'no'


def instance_exist(class_name, id):
    """Checks if an instance exists, if so return 'yes'
    else 'no'"""

    result = class_exist(class_name)
    if result == 'yes':
        if f"{class_name}.{id}" in FileStorage().all().keys():
            return 'yes'
        else:
            return 'no'


def attribute_exist(self, class_name, id, attribute):
    """Checks if an attributes exists, if so return 'yes'
    else return 'no'"""

    result = self.instance_exist(class_name, id)
    if result == 'yes':
        if attribute in FileStorage(

        ).all()[f"{class_name}.{id}"].to_dict().values():
            return 'yes'
        else:
            return 'no'
    return 'no'
