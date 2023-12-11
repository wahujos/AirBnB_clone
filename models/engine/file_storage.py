#!/usr/bin/python3
"""The class to store"""
import json
import os


class FileStorage:
    """
    class that serializes instances to a JSON file and deserializes
    JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Public instance method that return the dictionary object"""

        return self.__objects

    def new(self, obj):
        """Public instance method that set in object with key"""

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """instance method that serializes object to json file"""

        object_dict = {key: obj.to_dict() for key, obj
                       in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(object_dict, file)

    def reload(self):
        """instance methods to deserilizes json file to objects"""

        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_load = json.load(file)

                from models.base_model import BaseModel
                from models.user import User
                from models.amenity import Amenity
                from models.city import City
                from models.place import Place
                from models.review import Review
                from models.state import State
                class_dict = {
                    'BaseModel': BaseModel,
                    'User': User,
                    'Amenity': Amenity,
                    'City': City,
                    'Place': Place,
                    'Review': Review,
                    'State': State
                    }

                for key, value in obj_load.items():
                    classname, object_id = key.split('.')
                    point = class_dict[classname]
                    FileStorage.__objects[key] = point(**value)
        except FileNotFoundError:
            pass
