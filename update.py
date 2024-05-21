#!/usr/bin/python3
import models

from console import HBNBCommand


def do_update(self, line):
    """Updates an existing instance's attribute or add a new attribute,
    instance id is Identified with <class name>.<object id>
    Usage:
    update <class name> <id> <attribute name> "<attribute value>
    """
    if self.assist_udpate(line) is False:
        return
    c_name, c_id, att_name, att_value = line.split(' ')
    object_update = self.hbnb_objects['{}.{}'.format(c_name,
                                                     c_id)]
    for type, key in self.types_dict.items():
        if att_name in key:
            setattr(object_update,  att_name, type(att_value))
        else:
            setattr(object_update, att_name,
                    str(att_value).partition('"')[2].removesuffix('"'))

    models.storage.save()


def update_base_on_class_name(line):
    """update an object"""
    c_name = line.split('.')[0]
    args = validate_update_args(line)

    if args:
        c_id, att_name, att_value = args
        object_update = HBNBCommand.hbnb_objects['{}.{}'.format(c_name, c_id)]
        for type, key in HBNBCommand().types_dict.items():
            if att_name in key:
                setattr(object_update,  att_name, type(att_value))
            else:
                setattr(object_update, att_name, str(att_value))

        models.storage.save()

        return


def validate_update_args(line):
    """# Usage: <class name>.update(<id>, <attr name>, <attr value>)"""
    c_name, update = line.split('.')
    update, args = update.split('(')
    args = args.split(',')

    if args == [')']:
        print("** instance id missing **")
        return
    elif len(args) == 1:
        print("** attribute name missing **")
        return
    elif len(args) == 2:
        print("** attribue value missing **")
        return
    elif len(args) == 3:
        id = args[0].partition('"')[2].removesuffix('"')
        att_name = args[1].partition('"')[2].removesuffix('"')
        att_v = args[2].partition('"')[2].removesuffix(')').removesuffix('"')

        if id == '':
            print('** instance id missing **')
        elif att_name == '':
            print('** attribue name missing')
        elif att_v == '':
            print('** attribute value missing **')

        id_exit = False
        for k, v in HBNBCommand().hbnb_objects.items():
            if id in k:
                id_exit = True

        if not id_exit:
            print("** no instance found **")
            return

        for count, arg in enumerate(args):
            args[count] = arg.partition('"')[2].removesuffix('"')
        return args
    return


def assist_udpate(line):
    """ This function checks if class exist, and if it is a valid class
    same goes for the id, attribute name and value of attribute"""

    update_attr = line.split(' ')
    update_attr_len = len(update_attr)

    if update_attr == ['']:
        print('** class name missing **')
        return False
    elif update_attr_len == 1:
        print('** instance id missing **')
        return False
    elif update_attr_len == 2:
        print('** attribute name missing **')
        return False
    elif update_attr_len == 3:
        print('** instance value missing **')
        return False
    elif update_attr_len == 4:
        c_name, id, attr_name, attr_value = update_attr

        if c_name not in HBNBCommand.hbnb_classess:
            print('** class name not found **')
            return False
        elif '{}.{}'.format(c_name,
                            id) not in HBNBCommand.hbnb_objects.keys():
            print("** no instance found **")
