#!/usr/bin/python3

from models.base_model import BaseModel
"""Dealing with all relevant imports"""


class User(BaseModel):
    """
    Defining the User class that inherits from the Base class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
