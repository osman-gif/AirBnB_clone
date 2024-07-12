#!/usr/bin/python3
""" This is the AirBnbClone console project, In this project I'am creating
a command_line interpreter for the AirBnbClone project """

import cmd
import re
import models.base_model as base_model
from models.user import User
from models.base_model import BaseModel
import models
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
import update
import show


class HBNBCommand(cmd.Cmd):

    hbnb_objects = models.storage.all()
    hbnb_classess = ['BaseModel', 'User',
                     'State', 'City', 'Amenity', 'Review', 'Place']
    classes_dict = {'BaseModel': BaseModel, 'User': User,
                    'State': State, 'City': City,
                    'Amenity': Amenity, 'Place': Place, 'Review': Review}
    prompt = '(hbnb)'
    str_types = ['name', 'state_id', 'city_id',
                 'user_id', 'description', 'place_id', 'text']
    int_types = ['number_rooms', 'number_bathrooms',
                 'max_guest', 'price_by_night']
    float_types = ['longitude', 'latitude']

    types_dict = {str: str_types, int: int_types, float: float_types}

    def do_quit(self, line):
        """ Implements the quit command, exiting the interpreter
        Usage:
            quit"""
        return True

    def do_EOF(self, line):
        """ Exit the interpreter if EOF detected"""
        return True

    def emptyline(self):
        """ Empty line does nothing"""
        pass

    # __________ console.py v-0.1 _________

    def class_exist(self, line, classes):
        """Checks if a class exists"""
        if not line:
            print("** class name missing **")
            return False
        elif line not in self.hbnb_classess:
            print("** class doesn't eixst **")
            return False
        else:
            return True

    def do_create(self, line):
        """Creates a BaseModel object, saves it to a json file and prints it ID
      Usage:
        Create <class name>"""

        if self.class_exist(line, self.hbnb_classess) is False:
            return
        for k, v in self.classes_dict.items():
            
            if line == k:
                my_classs = v()
                models.storage.save()
                print(my_classs.id)

    def do_show(self, line):
        show.do_show(self, line)

    def do_destroy(self, line):
        """ Deletes  an object
        based on class name and object id
        Usage:
        destroy <class name> <object id>"""

        # check class name exist
        if line.split(' ') == ['']:
            print('** class name missing **')
            return
        if len(line.split(' ')) == 1:
            print('** instance id missing **')
            return

        c_name, o_id = line.split(' ')

        if self.class_exist(c_name, self.hbnb_classess) is False:
            return
        elif '{}.{}'.format(c_name, o_id) in self.hbnb_objects.keys():
            del self.hbnb_objects['{}.{}'.format(c_name, o_id)]
            models.storage.save()
        else:
            print('** no instance found **')

    def do_all(self, line):
        """ Lists all objects based or not on the class name.
        Usage:
        -with all class:
            Usage: all
        -with specific class:
            Usage: all <class name>"""

        obj_list = []
        if line:
            if line.split(' ')[0] not in self.hbnb_classess:
                print("** class doesn't exist **")
                return
            else:  # __________ specific class __________
                for k, v in self.hbnb_objects.items():
                    if k.split('.')[0] == line.split(' ')[0]:
                        obj_list.append('{}'.format(v))
                        # print(v)
                print(obj_list)
        else:  # __________ all class ___________
            for k, v in self.hbnb_objects.items():
                obj_list.append('{}'.format(v))
                # print(v)
            print(obj_list)

    def assist_udpate(self, line):
        update.assist_udpate(line)

    # _____________________________________________________________________

    def print_specific_class(self, line):
        """prints specific class objects"""
        c_name, all = line.split('.')
        my_list = []
        if c_name in self.hbnb_classess:
            for k, v in self.hbnb_objects.items():
                if c_name in k:
                    my_list.append('{}'.format(v))
        else:
            print("** class doesn't exist **")
        print(my_list)

    def show_or_destroy(self, line):
        show.show_or_destroy(self, line)

        # print("** no instance found **")
        # return

    def count(self, line):
        """counts objects"""
        c_name = line.split('.')

        count = 0
        for k, v in self.hbnb_objects.items():
            if c_name[0] in k:
                count = count + 1

        return count

    def evaluate_update_cmd(self, line):
        pass

    def onecmd(self, line):
        """onecmo function"""
        cmd_update = re.match(r'^.+\.update\(.*\)', line)
        all_classes = re.match(r'^.+\.all\(\)$', line)
        class_show = re.match(r'^.+\.show\(.*\)$', line)
        show_without_id = re.findall(r'^.+\.show\(\)', line)
        class_destroy_id = re.match(r'^.+\.destroy\(.+\)$', line)
        count_class_objects = re.match(r'^.+\.count\(\)', line)

        if cmd_update:
            update.update_base_on_class_name(line)
            return

        if count_class_objects:
            print(self.count(line))
            return
        if show_without_id:
            print(show_without_id)

        if all_classes:
            self.print_specific_class(line)
            return
        elif class_show or class_destroy_id:
            self.show_or_destroy(line)
            return
        elif re.match(r'^show()$', line):
            print('** class name missing **')
            return
        elif re.match(r'^.+\.show\(\)$',
                      line) or re.match(r'^.+\.destroy\(\)$', line):
            print("** instance id missing **")
            return

        return cmd.Cmd.onecmd(self, line)

# ________________________________________________________________________________________________
    def validate_update_args(self, line):
        update.validate_update_args(self, line)

    def update_base_on_class_name(self,  line):
        update.update_base_on_class_name(self, line)

    def do_update(self, line):
        update.do_update(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
