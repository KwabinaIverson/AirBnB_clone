#!/usr/bin/python3
"""class: FileStorage
`FileStorage` serializes instances to a JSON file and deserializes JSON file to instances."""

import json
from os.path import exists

class FileStorage():
    """`FileStorage Definition"""
    
    __file_path: str = 'file.json'
    __objects: dict = {}
    
    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
    
    def save(self):
        """Serializes `__objects` to the JSON file"""
        with open(self.__file_path, 'w') as json_file:
            json.dump(self.__objects, json_file)
    
    def reload(self):
        """
        Deserializes the JSON file to `__objects` (only if the JSON file `(__file_path)` exists ; otherwise, do nothing. 
        If the file doesn’t exist, no exception should be raised)
        """
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as json_file:
                self.__objects = json.load(json_file)
        else:
            self.__objects = {}
