#!/usr/bin/python3
"""
FileStorage Module: Defines the FileStorage class for serializing and deserializing instances to/from JSON files.
"""
import json
import models

class FileStorage:
    """
    FileStorage class serializes instances to JSON file and deserializes to JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """Adds a new object to __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes the objects into a JSON file"""
        objects_dict = {key: val for key, val in self.__objects.items()}
        with open(self.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """Reloads the file and deserializes JSON into __objects"""
        try:
            with open(self.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in self.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass
