import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_base_model_functionality(self):
        # Create a BaseModel instance
        my_model = BaseModel()

        # Set attributes
        my_model.name = "My First Model"
        my_model.my_number = 89

        # Assert initial string representation
        expected_string = "[BaseModel] ({}) {}".format(my_model.id,
                                                       my_model.__dict__)
        self.assertEqual(str(my_model), expected_string)

        # Save and assert updated string representation
        my_model.save()
        exp_upd = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertNotEqual(str(my_model), expected_string)
        self.assertEqual(str(my_model), exp_upd)

        # Convert to dictionary and assert attributes
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertEqual(my_model_json['name'], 'My First Model')
        self.assertEqual(my_model_json['my_number'], 89)
        self.assertEqual(my_model_json['id'], my_model.id)

        # Assert datetime strings
        self.assertIsInstance(my_model_json['created_at'], str)
        self.assertIsInstance(my_model_json['updated_at'], str)

        # Convert datetime strings back to datetime objects and assert
        created_at = datetime.strptime(my_model_json['created_at'],
                                       '%Y-%m-%dT%H:%M:%S.%f')
        updated_at = datetime.strptime(my_model_json['updated_at'],
                                       '%Y-%m-%dT%H:%M:%S.%f')
        self.assertIsInstance(created_at, datetime)
        self.assertIsInstance(updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
