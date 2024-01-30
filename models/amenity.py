"""
Create Ameinty class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This is amenity class
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """ This Initialize the Amenity objects"""
        super().__init__(*args, **kwargs)
