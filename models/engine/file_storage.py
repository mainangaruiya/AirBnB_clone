#!/usr/bin/python3
"""Module defining the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Class for file storage."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return type(self).__objects

    def new(self, obj):
        """Set in __objects obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        type(self).__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        with open(type(self).__file_path, mode='w', encoding='utf-8') as f:
            obj_dict = {}
            for key, obj in type(self).__objects.items():
                obj_dict[key] = obj.to_dict()
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file (path: __file_path) to __objects."""
        try:
            with open(type(self).__file_path, mode='r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, obj_attrs in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    obj_attrs['__class__'] = cls_name
                    obj = eval(cls_name + "(**obj_attrs)")
                    type(self).__objects[key] = obj
        except FileNotFoundError:
            pass

