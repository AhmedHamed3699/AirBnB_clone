#!/usr/bin/python3
"""This is a module for file storage."""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    A class for file storage.

    It is responsible for:
    - serializing instances to a JSON file
    - deserializing JSON files to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Get all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set obj in objects."""
        obj_dict = obj.to_dict()
        key = str(obj_dict['__class__']) + '.' + str(obj_dict['id'])
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize objects to the JSON file."""
        all_objects = FileStorage.__objects.copy()
        for key, value in all_objects.items():
            all_objects[key] = value.to_dict()
        json_string = json.dumps(all_objects)
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            file.write(json_string)

    def reload(self):
        """Deserialize the JSON file to objects."""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                json_string = file.read()
            all_objects = json.loads(json_string)
            for key, value in all_objects.items():
                if value['__class__'] == 'BaseModel':
                    all_objects[key] = BaseModel(**value)
                elif value['__class__'] == 'User':
                    all_objects[key] = User(**value)
            FileStorage.__objects = all_objects
        except FileNotFoundError:
            return
