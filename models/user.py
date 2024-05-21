#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """User"""

    # ___________ puplic attributes ____________
    email = ""
    password = ""
    first_name = ""
    last_name = ""
