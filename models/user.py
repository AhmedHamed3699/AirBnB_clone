#!/usr/bin/python3
"""This is a module for user model."""
from models.base_model import BaseModel


class User(BaseModel):
    """A class for user that inherits from BaseModel."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *_args, **kwargs):
        """Construct a new object."""
        super().__init__(kwargs)
