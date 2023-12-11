#!/usr/bin/python3
"""base module for other classes"""
from uuid import uuid4
from datetime import datetime
from models import storage
import models


class BaseModel:
    """base that defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """iniatializing the model"""

        datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, datetime_format)

                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """definig str that print"""

        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        """method that update public instance attribute of updated date"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """instance that returns a dictionary containing all keys/values"""

        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        # obj["id"] = self.id
        return obj_dict

    # @staticmethod
    # def from_dict(obj_dict):
    #     obj = BaseModel()
    #     for key, value in obj_dict.items():
    #         if key == 'created_at' or key == 'updated_at':
    #             value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
    #         if key != "__class__":
    #             setattr(obj, key, value)
    #     return obj
