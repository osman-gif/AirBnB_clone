#!/usr/bin/python3
import models
console = __import__("console")
# from console import HBNBCommand


def show_or_destroy(self, line):
    """ Shows an object or destroys it"""
    classes = console.HBNBCommand.hbnb_classess
    objects = console.HBNBCommand.hbnb_objects
    """ Destroys and object"""

    c_name, fun_id = line.split('.')
    if self.class_exist(c_name, classes) is False:
        return

    fun_id = fun_id.split('(')
    id = fun_id[1].removesuffix(')')
    fun = fun_id[0]

    id = id.partition('"')[2].removesuffix('"')

    for k, v in objects.items():
        if '{}.{}'.format(c_name, id) == k:
            if fun == 'show':
                print(v)
                return

            elif fun == 'destroy':
                # if id in k:
                temp_list = objects.copy()
                del temp_list['{}.{}'.format(c_name, id)]
                objects = temp_list
                return
    print("** no instance found **")
    return


def do_show(self, line):
    """Shows an object"""
    classes = console.HBNBCommand.hbnb_classess
    objects = console.HBNBCommand.hbnb_objects
    """ Prints the string representation of an object
    based on class name and object id
    Usage:
        show <class name> <object id>"""

    # check class name exist
    if line.split(' ') == ['']:
        print('** class name missing **')
        return
    if len(line.split(' ')) == 1:
        print('** instance id missing **')
        return

    c_name, o_id = line.split(' ')

    if self.class_exist(c_name, classes) is False:
        return
    elif '{}.{}'.format(c_name, o_id) in objects.keys():
        print(objects['{}.{}'.format(c_name, o_id)])
    else:
        print('** no instance found **')
