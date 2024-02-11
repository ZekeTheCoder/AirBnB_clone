#!/usr/bin/env python3
"""
Unittest for BaseModel class
"""
import unittest
import pep8
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up a BaseModel instance with some attributes.
        it is called once before any tests in the class are run"""
        cls.my_model = BaseModel()
        cls.my_model.name = "My First Model"
        cls.my_model.my_number = 89

    @classmethod
    def tearDownClass(cls):
        """Clean up the BaseModel instance."""
        del cls.my_model

# Test code structure

    def test_style(self):
        """Test if file complies with the PEP 8 style guide"""
        file_style = pep8.StyleGuide(quiet=True)
        style = file_style.check_files(['models/base_model.py'])
        self.assertEqual(style.total_errors, 0, "fix pep8")

    def test_doc_string(self):
        """Test BaseModel class docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

# Test functionality

    def test_attributes(self):
        """Test for attributes in BaseModel class"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        """Test class initializer"""
        self.assertTrue(isinstance(self.my_model, BaseModel))

    def test_string_representation(self):
        """Test if the string representation of the BaseModel is correct."""
        expected_string = "[BaseModel] ({}) {}".format(self.my_model.id,
                                                       self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected_string)

    def test_save_method(self):
        """Test if the save method updates the BaseModel instance correctly"""
        expected_string = "[BaseModel] ({}) {}".format(self.my_model.id,
                                                       self.my_model.__dict__)
        self.my_model.save()
        updated_string = "[BaseModel] ({}) {}".format(self.my_model.id,
                                                      self.my_model.__dict__)
        self.assertNotEqual(str(self.my_model), expected_string)
        self.assertEqual(str(self.my_model), updated_string)

    def test_to_dict_method(self):
        """Test if the to_dict method of the BaseModel class correctly
        converts the instance to a dictionary."""
        my_model_json = self.my_model.to_dict()
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertEqual(my_model_json['name'], 'My First Model')
        self.assertEqual(my_model_json['my_number'], 89)
        self.assertEqual(my_model_json['id'], self.my_model.id)
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)

    def test_datetime_conversion(self):
        """Test if datetime strings are correctly converted to
        datetime objects."""
        my_model_json = self.my_model.to_dict()
        created_at = datetime.strptime(my_model_json['created_at'],
                                       '%Y-%m-%dT%H:%M:%S.%f')
        updated_at = datetime.strptime(my_model_json['updated_at'],
                                       '%Y-%m-%dT%H:%M:%S.%f')
        self.assertIsInstance(created_at, datetime)
        self.assertIsInstance(updated_at, datetime)

    def test_init_with_keyword_arguments(self):
        """Test initialization with keyword arguments"""
        my_model = BaseModel(name="Thabang Maphanisane", my_number=23)
        self.assertEqual(my_model.name, "Thabang Maphanisane")
        self.assertEqual(my_model.my_number, 23)

    def test_date_time_conversion(self):
        """Test automatic conversion of date-time strings"""
        kwargs = {
            "created_at": "2024-02-11T17:15:06.202083",
            "updated_at": "2024-02-11T17:15:06.202095"
        }
        my_model = BaseModel(**kwargs)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_default_initialization(self):
        """Test default initialization"""
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
