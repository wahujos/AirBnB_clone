#!/usr/bin/python3
"""This is the test file for the review class"""
import unittest
from models.review import Review
from models.base_model import BaseModel
import models
from datetime import datetime


class TestReview(unittest.TestCase):
    """testing the review"""

    def init_test(self):
        """ Test the initialization """

        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

    def test_id_initialisation(self):
        """test id init"""

        rev_1 = Review()
        rev_2 = Review(1)
        self.assertIsInstance(rev_1, Review)
        self.assertTrue(hasattr(rev_1, "id"))
        self.assertNotEqual(rev_1.id, rev_2.id)
        self.assertIsInstance(rev_2.id, str)

    def test_attr_init(self):
        """testing attribute of review"""

        rev_1 = Review()
        rev_2 = Review()
        self.assertTrue(hasattr(rev_1, "text"))
        self.assertTrue(hasattr(rev_1, "place_id"))
        self.assertTrue(hasattr(rev_1, "user_id"))
        self.assertIsInstance(rev_1.created_at, datetime)
        self.assertIsInstance(rev_1.updated_at, datetime)
        self.assertIsInstance(rev_1.text, str)
        self.assertIsInstance(rev_1.user_id, str)
        self.assertIsInstance(rev_1.place_id, str)
        self.assertNotEqual(rev_2.created_at, rev_1.created_at)
        self.assertNotEqual(rev_1.updated_at, rev_2.updated_at)

    def test_kwargs_initialize(self):
        """test the kwarg"""

        my_dict = {
                'id': 'c66c9cf9-91e8-44e4-babf-4e39e2817edd',
                'created_at': '2023-12-11T21:03:54.052298',
                '__class__': 'Review',
                'my_number': 73,
                'updated_at': '2023-12-11T21:03:54.052302',
                'text': 'My review'
                }

        rev = Review(**my_dict)
        self.assertNotIn("__class__", rev.__dict__)
        self.assertDictEqual(my_dict, rev.to_dict())
        self.assertIsInstance(rev.created_at, datetime)
        self.assertIsInstance(rev.updated_at, datetime)

    def test_kwargs_empty(self):
        """test for empty kwarg"""

        self.assertIn(Review(), models.storage.all().values())

    def test_save(self):
        """test save"""

        review = Review()
        review.save()
        self.assertNotEqual(review.created_at, review.updated_at)
        with self.assertRaises(TypeError):
            review.save(None)

    def test_to_dict(self):
        """test conversion to dict"""

        rev = Review()
        rev_dict = rev.to_dict()
        self.assertIsInstance(rev_dict, dict)
        for key in rev_dict.keys():
            self.assertIsInstance(rev_dict[key], str)

    def test_to_dict_arguments(self):
        """testing for argynent error"""

        review = Review()
        with self.assertRaises(TypeError):
            review.to_dict(None)

    def test_to_dict_attr(self):
        """tests to dict attributes"""

        review = Review()
        review.text = "My first review"
        self.assertIn("__class__", review.to_dict())
        self.assertIn("text", review.to_dict())
        self.assertNotEqual(review.__dict__, review.to_dict())


if __name__ == '__main__':
    unittest.main()
