#!/usr/bin/python3
"""UniqueCity Module"""
from unique_models.base_model import UniqueBaseModel


class UniqueCity(UniqueBaseModel):
    """
    Class for representing a city, inherits from UniqueBaseModel
    The public class attributes should be empty
    """
    state_id = ""
    name = ""
