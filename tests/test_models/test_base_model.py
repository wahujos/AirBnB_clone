#!/usr/bin/python3
"""Unit test for the base class"""


import unittest
from uuid import uuid4
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init_(self):
        """test initialization instances"""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsNotNone(instance.id)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertNotEqual(instance.created_at, instance.updated_at)

    def test_id_init(self):
        """test initiization id"""
        base_1 = BaseModel()
        base_2 = BaseModel(1)
        self.assertIsInstance(base_1, BaseModel)
        self.assertIsInstance(base_2.id, str)
        self.assertNotEqual(base_1.id, base_2.id)

    def test_attr_init(self):
        base = BaseModel(None)
        base.name = "My Model"
        base.number = 73
        self.assertTrue(hasattr(base, "name"))
        self.assertTrue(hasattr(base, "number"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

    def test_kwargs(self):
        my_dict = {
                'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                'created_at': '2017-09-28T21:03:54.052298',
                '__class__': 'BaseModel',
                'my_number': 73,
                'updated_at': '2017-09-28T21:03:54.052302',
                'name': 'My_Model'
                }
        Model_dict = BaseModel(**my_dict)

        self.assertNotIn("__class__", Model_dict.__dict__)
        self.assertDictEqual(my_dict, Model_dict.to_dict())
        self.assertIsInstance(Model_dict.created_at, datetime)
        self.assertIsInstance(Model_dict.updated_at, datetime)

    def test_str_method(self):
        model = BaseModel()
        expected_output = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_output)

    def test_save_method(self):
        base = BaseModel()
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)

    def test_date_updated(self):
        Model = BaseModel()
        old_updated_at = Model.updated_at
        sleep(0.1)
        Model.save()
        new_updated_at = Model.updated_at
        self.assertNotEqual(new_updated_at, old_updated_at)

    def test_to_dict_method(self):
        obj_dict = BaseModel().to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(datetime.fromisoformat(obj_dict['created_at']),
                              datetime)
        self.assertIsInstance(datetime.fromisoformat(obj_dict['updated_at']),
                              datetime)

    def test_args_dict(self):
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.to_dict(None)


if __name__ == '__main__':
    unittest.main
