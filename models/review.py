#!/usr/bin/python3
"""This is a module for review model."""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class for review that inherits from BaseModel."""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *_args, **kwargs):
        """Construct a new object."""
        super().__init__(**kwargs)
