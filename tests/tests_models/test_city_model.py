#!/usr/bin/python3

"""
Test for the City model.
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    Testing City class
    """

    def test_City_inheritance(self):
        """
        Tests that the City class inherits from BaseModel
        """
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    def test_City_attributes(self):
        """
        Tests that City class has state_id and name attributes.
        """
        new_city = City()
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())

    def test_type_name(self):
        """
        Test the type of name attribute.
        """
        new_city = City()
        name = getattr(new_city, "name")
        self.assertIsInstance(name, str)

    def test_type_state_id(self):
        """
        Test the type of state_id attribute.
        """
        new_city = City()
        state_id = getattr(new_city, "state_id")
        self.assertIsInstance(state_id, str)


if __name__ == '__main__':
    unittest.main()
