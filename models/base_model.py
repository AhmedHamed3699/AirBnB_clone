#!/usr/bin/python3
"""This is a module for the base model."""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """A class that defines all common attributes/methods for other classes."""

    def __init__(self):
        """Construct a new object."""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Convert object to string."""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Update object."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert object to dictionary."""
        dict_obj = self.__dict__
        dict_obj['__class__'] = 'BaseModel'
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj
