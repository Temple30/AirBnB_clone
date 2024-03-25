#!/usr/bin/python3

"""
All the tests for the BaseModel are implemented here.
"""

import unittest
from models.base_model import BaseModel
from io import StringIO
import sys
import datetime


class TestBaseModel(unittest.TestCase):
    """
    Testing the BaseModel class.
    """

    def setUp(self):
        """
        Initialize instance.
        """
        self.my_model = BaseModel()
        self.my_model.name = "Binita Rai"

    def tearDown(self):
        """
        Remove instance.
        """
        del self.my_model

    def test_id_type(self):
        """
        Checks that the type of the id is string.
        """
        self.assertEqual(str, type(self.my_model.id))

    def test_ids_differ(self):
        """
        Checks that the ids between two instances are different.
        """
        new_model = BaseModel()
        self.assertNotEqual(new_model.id, self.my_model.id)

    def test_name(self):
        """
        Checks that an attribute can be added.
        """
        self.assertEqual("Binita Rai", self.my_model.name)

    def test_a_updated_created_equal(self):
        """
        Checks that both dates are equal.
        """
        self.assertEqual(self.my_model.updated_at.year,
                         self.my_model.created_at.year)

    def test_save(self):
        """
        Checks that after updating the instance, the dates differ in the
        updated_at attribute.
        """
        old_update = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, old_update)

    def test_str_override(self):
        """
        Checks that the right message gets printed.
        """
        backup = sys.stdout
        inst_id = self.my_model.id
        capture_out = StringIO()
        sys.stdout = capture_out
        print(self.my_model)

        cap = capture_out.getvalue().split(" ")
        self.assertEqual("[BaseModel]", cap[0])
        self.assertEqual("({})".format(inst_id), cap[1])
        sys.stdout = backup

    def test_to_dict_type(self):
        """
        Checks that the to_dict method return type.
        """
        self.assertEqual(dict, type(self.my_model.to_dict()))

    def test_to_dict_class(self):
        """
        Checks that the __class__ key exists.
        """
        self.assertEqual("BaseModel", self.my_model.to_dict()["__class__"])

    def test_to_dict_type_updated_at(self):
        """
        Checks the type of the value of updated_at.
        """
        self.assertEqual(str, type(self.my_model.to_dict()["updated_at"]))

    def test_to_dict_type_created_at(self):
        """
        Checks the type of the value of created_at.
        """
        tmp = self.my_model.to_dict()
        self.assertEqual(str, type(tmp["created_at"]))

    def test_kwargs_instantiation(self):
        """
        Test that an instance is created using the key value pair.
        """
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        self.assertEqual(new_model.id, self.my_model.id)

    def test_type_created_at(self):
        """
        Test that the new_model's updated_at data type is datetime.
        """
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertIsInstance(new_model.created_at, datetime.datetime)

    def test_type_updated_at(self):
        """
        Test that the new_model's created_at data type is datetime.
        """
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertIsInstance(new_model.updated_at, datetime.datetime)

    def test_compare_dict(self):
        """
        Test that the new_model's and my_model's dictionary values are the same.
        """
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        new_model_dict = new_model.to_dict()
        self.assertEqual(my_model_dict, new_model_dict)


if __name__ == '__main__':
    unittest.main()
