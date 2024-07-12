#!/usr/bin/python3

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


class FileStorage():
    """
    This models the Filestorage storage type, it has functions for serializing
    python dictionary to json, and deserializing json back to python dictionary
    """

    __file_path = 'file.json'
    __objects = {}

    @property
    def get_file_path(self):
        """
        return the file path
        """
        return self.__file_path

    @property
    def get_objects(self):
        """
        Returns the __objects variable
        """
        return self.__objects

    def all(self):
        """
        returns the __objects variable, all objects
        """
        return self.__objects

    def new(self, obj):
        """
        adds the newly created object 'obj' to __.objects dictionary
        """
        self.__objects['{}.{}'.format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Convert the dictionary of objects '__objects' into json format and
        save it into a json file that it creates
        """
        new_dict = {}
        for k, v in self.__objects.items():
            new_dict[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            # print(new_dict)
            json.dump(new_dict, file)

    def reload(self):
        """
        Reads the contents of the json file, convert them from json
        to python dictionary and recreate objects from this dictionary and save
        those recreated objects into '__objects' dictionary
        """
        new_dict = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding='utf-8') as file:
                new_dict = json.load(file)
            for k, v in new_dict.items():
                match k.split('.')[0]:
                    case 'User':
                        self.__objects[k] = User(**v)
                    case 'BaseModel':
                        self.__objects[k] = BaseModel(**v)
                    case 'Place':
                        self.__objects[k] = Place(**v)
                    case 'Amenity':
                        self.__objects[k] = Amenity(**v)
                    case 'Review':
                        self.__objects[k] = Review(**v)
                    case 'City':
                        self.__objects[k] = City(**v)
                    case 'State':
                        self.__objects[k] = State(**v)
