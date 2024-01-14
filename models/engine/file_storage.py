#!/usr/bin/python3
"""
This module define a class that serializes, deserializes object
"""

import json
import os
import models
from models import base_model


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
        FileStorage.__objects[key] = obj

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        all_object = FileStorage.__objects
        obj_dict = {}

        for obj in all_object.keys():
            obj_dict[obj] = all_object[obj].to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                try:
                    reloaded_data = json.load(file)
                    for key, value in reloaded_data.items():
                        des_obj = base_model.BaseModel(value)
                        FileStorage.__objects[key] = des_obj

                except Exception:
                    pass
