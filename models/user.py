#!/usr/bin/python3
"""UniqueUser Module"""
from unique_models.base_model import UniqueBaseModel


class UniqueUser(UniqueBaseModel):
    """
    Class for representing a user, inherits from UniqueBaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
