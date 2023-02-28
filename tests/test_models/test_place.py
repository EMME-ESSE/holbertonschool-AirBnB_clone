#!/usr/bin/python3
"""
testing class Review
"""

import unittest
from models import place
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class test_class_base(unittest.TestCase):
    """class for testing class Review"""

    @classmethod
    def setUpClass(self):
        """set class"""
        self.my_model = Place()

    def test_docmodule(self):
        """checking doc module"""
        self.assertIsNotNone(place.__doc__)

    def test_docclass(self):
        """checking doc class"""
        self.assertIsNotNone(Place.__doc__)

    def test_create(self):
        """test instance class"""
        self.assertIsInstance(self.my_model, Place)
        self.assertTrue(issubclass(Place, BaseModel), True)

    def test_attr(self):
        """test attributes"""
        self.assertEqual(type(self.my_model.id), str)
        self.assertEqual(type(self.my_model.created_at), datetime)
        self.assertEqual(type(self.my_model.updated_at), datetime)

    def test_class(self):
        """ test class """
        self.assertTrue(issubclass(Place, BaseModel))


if __name__ == "__main__":
    unittest.main()
