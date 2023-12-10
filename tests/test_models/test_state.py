#!/usr/bin/python3
"""test for state class"""
import unittest
from datetime import datetime
import json
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """Testing the state class"""

    def setUp(self):
        """This function is run before the test are done"""
        self.state = State()
        self.state.name = "Nairobi"

    def test_state_instance(self):
        """This function tests whether the instances are created correctly"""
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)

    def test_state_attributes(self):
        """This function test the attributes of the class"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))

    def test_state_attribute_type(self):
        """
        This function test whether the particular attributes
        of the class are of the correct type
        """
        self.assertIsInstance(self.state.name, str)
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_state_to_dict(self):
        """Test the to dict function with this class"""
        state_dict = self.state.to_dict()

        self.assertIsInstance(state_dict, dict)
        self.assertIn('name', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertEqual(state_dict['name'], "Nairobi")

    def test_state_str(self):
        """Test whrther the string representation gives the correct output"""
        class_name = self.state.__class__.__name__
        identity = self.state.id
        obj_dict = self.state.__dict__
        estr = "[{}] ({}) {}".format(class_name, identity, obj_dict)
        self.assertEqual(str(self.state), estr)

    def test_state_save(self):
        """Tests whether the save function saves correctly"""
        initial_updated = self.state.updated_at
        self.state.save()
        self.assertNotEqual(initial_updated, self.state.updated_at)

    def test_state_serialization(self):
        """Test the serialization and the deserialization"""
        state_json = json.dumps(self.state.to_dict())
        new_state_dict = json.loads(state_json)
        new_state = State(**new_state_dict)

        self.assertIsInstance(new_state, State)
        self.assertEqual(self.state.id, new_state.id)
        self.assertEqual(self.state.name, new_state.name)
        self.assertEqual(self.state.created_at, new_state.created_at)
        self.assertEqual(self.state.updated_at, new_state.updated_at)
