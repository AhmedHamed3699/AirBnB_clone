#!/usr/bin/python3
"""This is a module for place model."""
from models.base_model import BaseModel


class Place(BaseModel):
    """A class for place that inherits from BaseModel."""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *_args, **kwargs):
        """Construct a new object."""
        super().__init__(kwargs)
