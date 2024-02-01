#!/usr/bin/python3
""" This is review module """
from models.base_model import BaseModel


class Review(BaseModel):
    """ This is Review class """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ This Initialize the review object"""
        super().__init__(*args, **kwargs)
