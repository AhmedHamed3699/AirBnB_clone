#!/usr/bin/python3
"""This is a module for amenity model."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class for amenity that inherits from BaseModel."""

    name = ""

    def __init__(self, *_args, **kwargs):
        """Construct a new object."""
        super().__init__(**kwargs)
