#!/usr/bin/python3

import datetime
import uuid
file_storage = __import__('models')
# from models import storage
""" This is the AirBnbClone console project """


class BaseModel():

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            file_storage.storage.new(self)

        else:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k in ['created_at', 'updated_at']:
                        setattr(self, k, datetime.datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)

    def __str__(self):
        new_dict = {}
        for key, value in self.__dict__.items():
            new_dict[key] = value
        class_dict = {'id': self.id, 'created_at': self.created_at,
                      'updated_at': self.updated_at}.items()
        for key, value in class_dict:
            new_dict[key] = value
        new_dict['__class__'] = self.__class__.__name__
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, new_dict)

    def save(self):
        self.updated_at = datetime.datetime.now()
        file_storage.storage.save()

    def to_dict(self):
        new_dict = {}
        class_dict = {'id': self.id, 'created_at': str(self.created_at),
                      'updated_at': str(self.updated_at)}
        for key, value in self.__dict__.items():
            new_dict[key] = value
        for key, value in class_dict.items():
            new_dict[key] = value
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
