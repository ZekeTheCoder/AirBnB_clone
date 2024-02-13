#!/usr/bin/env python3
"""
Unittest for FileStorage class
"""

import os
import json
import pep8
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class FileStorageTests(unittest.TestCase):
    """ class of File Storage Tests """

    def setUp(self):
        """ called before each test method in the test class """
        self.my_model = BaseModel()
        self.storage = FileStorage()

    def tearDown(self):
        """ called after each test method in the test class """
        # Remove any resources or objects created during testing
        self.my_model = None
        self.storage = None
        if os.path.exists(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

# Test code structure

    def test_style(self):
        """Test if FileStorage file complies with the PEP 8 style guide"""
        file_style = pep8.StyleGuide(quiet=True)
        style = file_style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(style.total_errors, 0, "fix pep8")

    def test_doc_string(self):
        """Test FileStorage class docstrings"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def testClassInstance(self):
        """ Check instance """
        self.assertIsInstance(storage, FileStorage)

    def testHasAttributes(self):
        """ verify if the FileStorage class has the attributes  """
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))

    def testSaveSelf(self):
        """Check save self"""
        msg = "save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            FileStorage().save(100)

        self.assertIn(msg, str(e.exception))

    def testsave(self):
        """verifies whether the save method of a model instance correctly
        saves data to a JSON file"""
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def testreload(self):
        """tests the reload method of the FileStorage class correctly
        reloads data from a JSON file """
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        dobj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(dobj, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(dobj[key].to_dict(), value.to_dict())

    def testReloadedObjects(self):
        """ Test printing reloaded objects """
        all_objects_in_storage = storage.all()
        print("-- Reloaded objects --")
        for obj_id in all_objects_in_storage.keys():
            obj = all_objects_in_storage[obj_id]
            print(obj)

    def testCreateNewObject(self):
        """ Test creating and saving a new object """
        self.my_model.name = "Thabang"
        self.my_model.my_number = 23
        self.my_model.save()
        print("-- Create a new object --")
        print(self.my_model)

        base_model_dict = self.my_model.to_dict()

        key = base_model_dict['__class__'] + "." + base_model_dict['id']

        self.assertTrue(key in storage.all())


if __name__ == "__main__":
    unittest.main()
