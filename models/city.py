#!/usr/bin/python3

from models.base_model import BaseModel

"""importing the base class module"""


class City(BaseModel):
    """
    Defining the City class that inherits from BaseModel class
    """
    state_id = ""
    name = ""
