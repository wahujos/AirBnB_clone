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
        return FileStorage.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        object_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(object_dict, file)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r') as file:
                    obj_load = json.load(file)

                    from models.base_model import BaseModel
                    class_dict = { 'BaseModel': BaseModel }
                    
                    for key, value in obj_load.items():
                        classname, object_id = key.split('.')
                        cls = class_dict[classname]
                        #instance = cls.from_dict(value)
                        cls_value = cls(**value)
                        FileStorage.__objects[key] = cls_value
            except FileNotFoundError:
                pass
