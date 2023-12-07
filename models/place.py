#!/usr/bin/python3

from models.base_model import BaseModel
"""Handling the imports of the Base class module"""


class Place(BaseModel):
    """
    Defining the class that inherits from the Base module
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""

    def __init__(self, city_id, user_id):
        """Defining the initialization class"""
        self.city_id = city_id
        self.user_id = user_id
