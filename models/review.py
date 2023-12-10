#!/usr/bin/python3
from models.base_model import BaseModel
"""importing the base class model"""


class Review(BaseModel):
    """
    Defining the Review class that inherits from the base class
    """
    place_id = ""
    user_id = ""
    text = ""
