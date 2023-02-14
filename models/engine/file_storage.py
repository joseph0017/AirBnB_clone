#!/usr/bin/python3
"""Module for file_storage"""
import json
from models.base_model import BaseModel


class FileStorage():
    """
    a class FileStorage that serializes instances to a
    JSON file and deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_d = FileStorage.__objects
        obj_json = {obj: json_d[obj].to_dict() for obj in json_d.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_json, file, default=lambda o: o.__dict__, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn’t exist, no exception should be raised
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                json_load = json.load(file)
            for k, v in json_load.items():
                FileStorage.__objects[k] = BaseModel(**v)
        except:
            pass

    def delete(self, obj=None):
        """delete objects from BaseModel"""
        if obj:
            try:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                del self.__objects[key]
                self.save()
            except:
                pass
