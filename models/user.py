"""
This User module
"""
import json
from models.base_model import BaseModel


class User(BaseModel):
    """
    This is class User
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize User class
        """
        super().__init__(*args, **kwargs)
