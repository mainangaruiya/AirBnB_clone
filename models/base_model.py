#!/usr/bin/python3
"""
This module defines a class BaseModel that defines all common attributes/methods
for other classes.
"""

import uuid
import datetime
from models import storage

class BaseModel:
    """
    This class defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the attributes of an instance.
        If kwargs is not empty, the attributes are initialized from kwargs.
        Otherwise, the attributes are initialized with default values.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Returns a string representation of an instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the attribute updated_at with the current datetime.
        Calls the save method of storage to serialize the instance.
        """
        self.updated_at = datetime.datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of an instance.
        """
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.iso

