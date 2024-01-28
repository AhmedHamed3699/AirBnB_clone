#!/usr/bin/python3
"""This is a module for city model."""
from models.base_model import BaseModel


class City(BaseModel):
    """A class for city that inherits from BaseModel."""

    state_id = ""
    name = ""

    def __init__(self, *_args, **kwargs):
        """Construct a new object."""
        super().__init__(**kwargs)
