#!/usr/bin/python3

"""
Test for the Place model.
"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Testing Place class
    """

    def setUp(self):
        """
        Creates an instance for place.
        """
        self.new_place = Place()

    def tearDown(self):
        pass

    def test_Place_inheritance(self):
        """
        Tests that the Place class Inherits from BaseModel
        """
        self.assertIsInstance(self.new_place, BaseModel)

    def test_Place_attributes(self):
        """
        Checks that the attributes exist.
        """
        attributes = [
            "city_id", "user_id", "description", "name",
            "number_rooms", "max_guest", "price_by_night",
            "latitude", "longitude", "amenity_ids"
        ]
        for attribute in attributes:
            self.assertTrue(attribute in self.new_place.__dir__())

    def test_attribute_types(self):
        """
        Tests the types of attributes.
        """
        attribute_types = {
            "city_id": str,
            "user_id": str,
            "description": str,
            "name": str,
            "number_rooms": int,
            "max_guest": int,
            "price_by_night": int,
            "latitude": float,
            "longitude": float,
            "amenity_ids": list
        }
        for attribute, attribute_type in attribute_types.items():
            value = getattr(self.new_place, attribute)
            self.assertIsInstance(value, attribute_type)


if __name__ == '__main__':
    unittest.main()
