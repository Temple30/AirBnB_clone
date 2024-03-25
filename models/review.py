#!/usr/bin/python3
"""UniqueReview Module"""
from unique_models.base_model import UniqueBaseModel


class UniqueReview(UniqueBaseModel):
    """
    Class for representing a review, inherits from UniqueBaseModel
    All attributes should be empty
    """
    place_id = ""
    user_id = ""
    text = ""
