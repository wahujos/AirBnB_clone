#!/usr/bin/python3
"""test for file storage class"""

import json
import unittest
import os
from unittest.mock import patch
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import models


class TestFileStorage(unittest.TestCase):
    """This is a class testing the File storage"""

    def test_init(self):
        "test_init if it works"
        storage = FileStorage()
        self.assertIsInstance(FileStorage(), FileStorage)
        self.assertTrue(hasattr(storage, '_FileStorage__objects'))
        self.assertTrue(hasattr(storage, '_FileStorage__file_path'))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
        with self.assertRaises(TypeError):
            FileStorage(None)

    def SetUp(self):
        """Test whether the all function actually returns a dictionary"""
        self.file_path = "file.json"
        with patch('models.engine.file_storage.FileStorage.__file_path',
                   self.file_path):
            self.storage = FileStorage()

    # def tearDown(self):
    #     """the tear down"""
    #     try:
    #         os.remove(self.storage._FileStorage__file_path)
    #     except FileNotFoundError:
    #         pass

    def test_all_empty(self):
        """test empty"""
        self.storage = FileStorage()
        self.assertNotEqual(self.storage.all(), {})

    def test_new(self):
        """Test new object sets in the object with the key specified"""
        self.storage = FileStorage()
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test whether the function serializes objects to json file"""
        self.storage = FileStorage()
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as file:
            key = "BaseModel.{}".format(model.id)
            self.assertIn(key, file.read())

    def test_reload(self):
        """test reload assertion"""
        self.storage = FileStorage()
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, all_objs.keys())
        self.assertNotEqual(len(all_objs), 1)

    def test_reload_file_not_found(self):
        """test reload method"""
        self.storage = FileStorage()
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        self.assertNotEqual(self.storage.all(), {})


if __name__ == '__main__':
    unittest.main()
