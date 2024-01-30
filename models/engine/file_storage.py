#!/usr/bin/python3
"""
This module define a class that serializes, deserializes object
"""

import json
import os
from models import base_model
from models import user
from models import city
from models import amenity
from models import state
from models import review
from models import place


class FileStorage:
    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        all_object = self.all()
        obj_dict = {}

        for key in all_object.keys():
            obj_dict[key] = all_object[key].to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """

        if os.path.exists(FileStorage.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                try:
                    reloaded_data = json.load(file)
                    for key, value in reloaded_data.items():
                        class_name, id = key.split('.')
                        match class_name:
                            case 'BaseModel':
                                des_obj = base_model.BaseModel(**value)
                            case 'User':
                                des_obj = user.User(**value)
                            case 'City':
                                des_obj = city.City(**value)
                            case 'Amenity':
                                des_obj = amenity.Amenity(**value)
                            case 'Review':
                                des_obj = review.Review(**value)
                            case 'State':
                                des_obj = state.State(**value)
                            case 'Place':
                                des_obj = place.Place(**value)

                        self.__objects[key] = des_obj

                except Exception:
                    pass

    def all_class_count(self, class_name):
        """
        This function returns the number of the instances of the
        class_name
        """

        all = self.__objects
        count = 0

        for key in all.keys():
            if str(class_name) == str(key.split('.')[0]):
                count = count + 1

        return count

    def destroy(self, id):
        """
        This function destroies an object
        """
        all = self.__objects
        id_exist = False
        my_key = 0
        for key in all.keys():
            if id == key.split('.')[1]:
                id_exist = True
                my_key = key
        if id_exist is True:
            print(key)
            if id in FileStorage().all().keys():
                print("ues")
                del FileStorage().__objects[my_key]
        print("** no instance found **")
