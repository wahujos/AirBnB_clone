#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """base that defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """iniatializing the model"""

        id = str(uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()
        date_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key == created_at or key == updated_at:
                    value = datetime.strptime(value, date_format)

                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        

    def __str__(self):
        classname = type(self).__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        """public instance to save date"""
        updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """instance that returns a dictionary containing all keys/values"""
        obj = self.__dict__.copy()
        obj["__class__"] = self.__class__.__name__
        obj["created_at"] = self.created_at.isoformat()
        obj["updated_at"] = self.updated_at.isoformat()
        obj["id"] = self.id
        return obj
