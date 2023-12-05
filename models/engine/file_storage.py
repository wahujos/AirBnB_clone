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
        object_dict = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(object_dict, file)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r') as file:
                    object_dict = json.load(file)
                    return object_dict
            except FileNotFoundError:
                pass
        else:
            return
