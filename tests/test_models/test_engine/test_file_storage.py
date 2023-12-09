#!/usr/bin/python3
"""test for file storage class"""

import json
import unittest
# from unittest.mock import patch, mock_open
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """This is a class testing the File storage"""
    def test_all(self):
        """Test whether the all function actually returns a dictionary"""
        self.storage = FileStorage()
        res = self.storage.all()
        self.assertIsInstance(res, dict)

    def test_new(self):
        """Test whether the new object sets in the object with the key specified"""
        self.storage = FileStorage()
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    # def test_save(self):
    #     """Test whether the function serializes objects to json file"""
    #     self.storage = FileStorage()
    #     with patch('builtins.open', create=True) as mock_open:
    #         self.storage.save()
    #         mock_open.assert_called_with(FileStorage._FileStorage__file_path, 'w')
    #         mock_open().write.assert_called()

    # def test_reload(self):
    #     """
    #     Test whether the function reload will deserialize the
    #     object from the file.read the contents of the file
    #     """
    #     self.storage = FileStorage()
    #     obj_dict = {'BaseModel.1': {'id': '1', 'name': 'example'}}
    #     with patch('builtins.open', create=True) as mock_open:

    #         mock_open().read.return_value = json.dumps(obj_dict)
    #         self.storage.reload()
    #         mock_open.assert_called_with(FileStorage._FileStorage__file_path, 'r')

    def test_reload(self):
        self.storage = FileStorage()
        obj_dict = {'BaseModel.1': {'id': '1', 'name': 'example'}}
        with patch('builtins.open', mock_open(read_data=json.dumps(obj_dict))):
            self.storage.reload()

    def test_save(self):
        self.storage = FileStorage()
        with patch('builtins.open', mock_open()) as mock_file:
            self.storage.save()
            mock_file.assert_called_once_with(FileStorage._FileStorage__file_path, 'w')
            mock_file().write.assert_called_once()
