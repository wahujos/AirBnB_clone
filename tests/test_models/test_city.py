#!/usr/bin/python
"""This is a test file for the city"""

import unittest
import json
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Testing the state class"""

    def setUp(self):
        """This function is run before the test are done"""
        self.city = City(state_id="state_123")

    def test_city_instance(self):
        """This function tests whether the instances are created correctly"""
        self.assertIsInstance(self.city, City)

    def test_city_inherits_from(self):
        """
        This function checks that the class inherits from Base Model
        """
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_attributes(self):
        """This function test the attributes of the class"""
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'state_id'))

    def test_city_attribute_type(self):
        """
        This function test whether the particular attributes
        of the class are of the correct type
        """
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)


if __name__ == '__main__':
    unittest.main()
