#!/usr/bin/python3
"""
This is City Model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ This is City class
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialzie the City class"""
        super().__init__(*args, **kwargs)
