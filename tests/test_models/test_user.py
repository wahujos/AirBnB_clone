#!/usr/bin/python3
"""test case for user class"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """Tesing the user class"""

    def test_init_user(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def setUp(self):
        self.store = FileStorage()
        self.store.reload()
        self.store._FileStorage__objects = {}

    def test_user(self):
        user = User()
        user.first_name = "Afeez"
        user.last_name = "Lasisi"
        user.email = "opeyemiolaafeez@gmail.com"
        user.password = "my_password"
        user.save()

        my_objs = self.store.all()
        key = f'User.{user.id}'
        self.assertIn(key, my_objs.keys())

    def teardown(self):
        self.store._FileStorage__objects = {}

    def test_user_to_dict(self):
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


if __name__ == '__main__':
    unittest.main()
