#!/usr/bin/python3
"""This is a module for state model."""
from models.base_model import BaseModel


class State(BaseModel):
    """A class for state that inherits from BaseModel."""

    name = ""

    def __init__(self, *_args, **kwargs):
        """Construct a new object."""
        super().__init__(kwargs)
