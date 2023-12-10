#!/usr/bin/python3
"""This is the place test file"""
import unittest
from models.place import Place
from models.base_model import BaseModel
from models.base_model import BaseModel
from datetime import datetime
import models


class TestPlace(unittest.TestCase):
    """ Testing the place"""

    def init_test(self):
        """ Test the initialization """

        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)

    def test_id_initialisation(self):
        """test id init"""

        plc_1 = Place()
        plc_2 = Place(1)
        self.assertIsInstance(plc_1, Place)
        self.assertTrue(hasattr(plc_1, "id"))
        self.assertNotEqual(plc_1.id, plc_2.id)
        self.assertIsInstance(plc_2.id, str)

    def test_attr_init(self):
        """testing attribute of review"""

        place1 = Place()
        place2 = Place()
        self.assertTrue(hasattr(place1, "city_id"))
        self.assertTrue(hasattr(place1, "name"))
        self.assertTrue(hasattr(place1, "user_id"))
        self.assertTrue(hasattr(place1, "description"))
        self.assertIsInstance(place1.created_at, datetime)
        self.assertIsInstance(place1.updated_at, datetime)
        self.assertIsInstance(place1.city_id, str)
        self.assertIsInstance(place1.name, str)
        self.assertIsInstance(place1.user_id, str)
        self.assertIsInstance(place1.description, str)
        self.assertNotEqual(place1.created_at, place2.created_at)
        self.assertNotEqual(place1.updated_at, place2.updated_at)
        self.assertIsInstance(place2.number_bathrooms, int)
        self.assertIsInstance(place2.number_rooms, int)
        self.assertIsInstance(place2.max_guest, int)
        self.assertIsInstance(place2.price_by_night, int)
        self.assertIsInstance(place2.latitude, float)
        self.assertIsInstance(place2.longitude, float)
        self.assertIsInstance(place2.amenity_ids, list)

    def test_kwargs_initialize(self):
        """test the kwarg"""

        my_dict = {
                'id': 'c66c9cf9-91e8-44e4-babf-4e39e2817edd',
                'created_at': '2023-12-11T21:03:54.052298',
                '__class__': 'Place',
                'my_number': 73,
                'updated_at': '2023-12-11T21:03:54.052302',
                'text': 'Hotel view'
                }

        place = Place(**my_dict)
        self.assertNotIn("__class__", place.__dict__)
        self.assertDictEqual(my_dict, place.to_dict())
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)

    def test_kwargs_empty(self):
        """test for empty kwarg"""

        self.assertIn(Place(), models.storage.all().values())

    def test_save(self):
        """test save"""

        place = Place()
        place.save()
        self.assertNotEqual(place.created_at, place.updated_at)
        with self.assertRaises(TypeError):
            place.save(None)

    def test_to_dict(self):
        """test conversion to dict"""

        plc = Place()
        plc_dict = plc.to_dict()
        self.assertIsInstance(plc_dict, dict)
        for key in plc_dict.keys():
            self.assertIsInstance(plc_dict[key], str)

    def test_to_dict_arguments(self):
        """testing for argynent error"""

        plc = Place()
        with self.assertRaises(TypeError):
            plc.to_dict(None)

    def test_to_dict_attr(self):
        """tests to dict attributes"""

        place = Place()
        place.text = "viewing review"
        self.assertIn("__class__", place.to_dict())
        self.assertIn("text", place.to_dict())
        self.assertNotEqual(place.__dict__, place.to_dict())


if __name__ == '__main__':
    unittest.main()
