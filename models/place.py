#!/usr/bin/python3
"""UniquePlace Module"""
from unique_models.base_model import UniqueBaseModel


class UniquePlace(UniqueBaseModel):
    """
    Class for representing a place, inherits from UniqueBaseModel
    All public class attributes should be empty
    """
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
