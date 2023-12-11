#!/usr/bin/python3
"""test case for user class"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import models
from datetime import datetime


class TestUser(unittest.TestCase):
    """Tesing the user class"""

    def test_init_user(self):
        """initialisation test"""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def setUp(self):
        """defining set up"""
        self.store = FileStorage()
        self.store.reload()
        self.store._FileStorage__objects = {}

    def test_user(self):
        """test user values"""
        user = User()
        user.first_name = "Afeez"
        user.last_name = "Lasisi"
        user.email = "opeyemiolaafeez@gmail.com"
        user.password = "my_password"
        user.save()

        my_objs = self.store.all()
        key = f'User.{user.id}'
        self.assertIn(key, my_objs.keys())

    # def teardown(self):
    #     """test the tear down"""
    #     self.store._FileStorage__objects = {}

    def test_user_to_dict(self):
        """test the user to dict"""
        user = User()
        user.first_name = "Afeez"
        user.last_name = "Lasisi"
        user.email = "opeyemiolaafeez@gmail.com"
        user.password = "my_password"
        user.save()
        user_dict = user.to_dict()
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('__class__', user_dict)
        self.assertIn('email', user_dict)
        self.assertIn('password', user_dict)
        self.assertIn('first_name', user_dict)
        self.assertIn('last_name', user_dict)

    def test_id_initialisation(self):
        """test id init"""

        rev_1 = User()
        rev_2 = User(1)
        self.assertIsInstance(rev_1, User)
        self.assertTrue(hasattr(rev_1, "id"))
        self.assertNotEqual(rev_1.id, rev_2.id)
        self.assertIsInstance(rev_2.id, str)

    def test_kwargs_empty(self):
        """test for empty kwarg"""

        self.assertIn(User(), models.storage.all().values())

    def test_attr_init(self):
        """testing attribute of review"""

        rev_1 = User()
        rev_2 = User()
        self.assertTrue(hasattr(rev_1, "email"))
        self.assertTrue(hasattr(rev_1, "password"))
        self.assertTrue(hasattr(rev_1, "first_name"))
        self.assertTrue(hasattr(rev_1, "last_name"))
        self.assertIsInstance(rev_1.created_at, datetime)
        self.assertIsInstance(rev_1.updated_at, datetime)
        self.assertIsInstance(rev_1.last_name, str)
        self.assertIsInstance(rev_1.email, str)
        self.assertIsInstance(rev_1.last_name, str)
        self.assertIsInstance(rev_1.first_name, str)
        self.assertIsInstance(rev_1.password, str)
        self.assertNotEqual(rev_2.created_at, rev_1.created_at)
        self.assertNotEqual(rev_1.updated_at, rev_2.updated_at)


if __name__ == '__main__':
    unittest.main()
