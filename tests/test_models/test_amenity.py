#!/usr/bin/python3
"""This is a test file for the ammenities class"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """This class tests that ammenities class"""

    def setUp(self):
        """This function is run before the tests are run"""
        self.amenity = Amenity()

    def test_amenity_instance(self):
        """Checks whether the instances are created correctly"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_amenity_inherits_basemodel(self):
        """Test whether ammenity is a subclasss of base model"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attribute_name_attribute(self):
        """Test the name attribute in the amenity class"""
        self.assertEqual(self.amenity.name, "")
        self.amenity.name = "Named Amenity"
        self.assertEqual(self.amenity.name, "Named Amenity")

    def test_amenity_from_dict(self):
        """Test the to dict function"""
        amenity_dict = {'id': 'test_id', 'name': 'Named Amenity'}
        amenity = Amenity(**amenity_dict)
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.id, 'test_id')
        self.assertEqual(amenity.name, 'Named Amenity')

    def test_amenity_str(self):
        class_name = self.amenity.__class__.__name__
        identity = self.amenity.id
        obj_dict = self.amenity.__dict__
        estr = "[{}] ({}) {}".format(class_name, identity, obj_dict)
        self.assertEqual(str(self.amenity), estr)


if __name__ == '__main__':
    unittest.main()
