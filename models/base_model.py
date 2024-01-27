#!/usr/bin/python3
"""
This defines BaseModel class
"""

from datetime import datetime
import uuid
import models

class BaseModel:
    """
    This class represent the parent class for all the other classes
    """

    def __init__(self, *args, **kwargs):
        """
        This method instantiate the class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """
        This method returns a string representation of the class
        """

        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        This method updates the updated_at attribute
        """

        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        This method returns a dictionary representation of the attributes
        of the object that is calling it
        """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
