#!/usr/bin/python3
"""Module for Base class"""

from datetime import datetime
import uuid


class BaseModel():
    """
    class BaseModel that defines all common
    attributes/methods for other classes:
    """
    def __init__(self, *args, **kwargs):
        """constuctor method"""
        if kwargs:
            for keys, values in kwargs.items():
                if keys == "created_at" or keys == "updated_at":
                    values == datetime.strptime(values, "%Y-%m-%dT%H:%M:%S.%f")
                if "__class__" != keys:
                    setattr(self, keys, values)
        
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()

    def __str__(self):
        """String Representation"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__
            )

    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the
        instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
