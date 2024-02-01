#!/usr/bin/python3
"""
This is the State Module
"""
from models.base_model import BaseModel


class State(BaseModel):
    """ This is the State class """

    name = ""

    def __init__(self, *args, **kwargs):
        """ This Initialize the State object """
        super().__init__(*args, **kwargs)
