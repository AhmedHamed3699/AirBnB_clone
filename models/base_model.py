#!/usr/bin/python3
"""This is a module for the base model."""
from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """A class that defines all common attributes/methods for other classes."""

    def __init__(self, *_args, **kwargs):
        """Construct a new object."""
        if kwargs:
            kwargs.pop('__class__', False)
            iso_format = kwargs['created_at']
            datetime_format = datetime.strptime(
                iso_format, "%Y-%m-%dT%H:%M:%S.%f")
            kwargs['created_at'] = datetime_format
            iso_format = kwargs['updated_at']
            datetime_format = datetime.strptime(
                iso_format, "%Y-%m-%dT%H:%M:%S.%f")
            kwargs['updated_at'] = datetime_format
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Convert object to string."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update object."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert object to dictionary."""
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = str(self.__class__.__name__)
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj
