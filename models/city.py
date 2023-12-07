#!/usr/bin/python3

from models.base_model import BaseModel

"""importing the base class module"""


class City(BaseModel):
    """
    Defining the City class that inherits from BaseModel class
    """
    state_id = ""
    name = ""

    def __init__(self, state_id):
        """
        defining the initialization function
        """
        self.state_id = state_id
