#!/usr/bin/python3
"""
This class Implementing serialization and deserialization using JSON
for the BaseModel class involves converting instances to and from JSON strings,
and then be stored in file.
"""


import os
import json


class FileStorage:
    """ Class that serializes and deserializes BaseModel instances
    to and from JSON """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Method returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name >.id
        to the JSON file
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        serialized_data = {}

        for key, obj in FileStorage.__objects.items():
            if not obj:
                pass
            else:
                serialized_data[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_data, file)

    def reload(self):
        """Deserializes __objects from the JSON file for BaseModel only."""
        from models.base_model import BaseModel
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    obj = BaseModel(**value)
                    self.__objects[key] = obj
