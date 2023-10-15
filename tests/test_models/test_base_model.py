#!/usr/bin/python3
"""
Test cases for BaseModel class
"""

import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel

class BaseModelTest(unittest.TestCase):
    """
    BaseModelTest class test the BaseModel class
    """
    
    def test_init__(self):
        """
        Test the `__init__()` method of the `BaseModel` class.
        """
        baseModel_instance = BaseModel()
        
        # Check if 'id' is a valid UUID version 4    
        self.assertTrue(uuid.UUID(baseModel_instance.id, version=4))
        
        # Check if 'id', 'create_at', and 'updated_at' is not None
        self.assertIsNotNone(baseModel_instance.id)
        self.assertIsNotNone(baseModel_instance.created_at)
        self.assertIsNotNone(baseModel_instance.updated_at)
        
    def test_init_with_kwargs(self):
        """
        Test the `__init__()` method of the `BaseModel` class with keyword arguments.
        """
        base_model = BaseModel(name='Alice', my_number=123)

        self.assertEqual(base_model.name, 'Alice')
        self.assertEqual(base_model.my_number, 123)
        
    def test_init_with_kwargs_datetime(self):
        """
        Test the `__init__()` method of the `BaseModel` class with keyword arguments for datetime fields.
        """
        created_at = '2023-10-11T14:43:38.559625'
        updated_at = '2023-10-11T14:43:38.559625'
        
        baseModel_instance = BaseModel(created_at=created_at, updated_at=updated_at)
        
        # Check if 'created_at' and 'updated_at' are datetime objects
        self.assertIsInstance(baseModel_instance.created_at, datetime)
        self.assertIsInstance(baseModel_instance.updated_at, datetime)
    
    def test_str(self):
        """
        Test the `__str__()` method of the `BaseModel` class.
        """
        base_model = BaseModel()

        expected_output = f'[{base_model.__class__.__name__}] ({base_model.id}) {base_model.__dict__}'
        self.assertEqual(str(base_model), expected_output)
    
    def test_save(self):
        """
        Test the `save()` method of the `BaseModel` class.
        """
        base_model = BaseModel()

        initial_updated_at = base_model.updated_at
        base_model.save()
        final_updated_at = base_model.updated_at
        self.assertGreater(final_updated_at, initial_updated_at)
    
    def test_to_dict(self):
        """
        Test the `to_dict()` method of the `BaseModel` class.
        """
        base_model = BaseModel(name='Alice', my_number=123)

        dict_representation = base_model.to_dict()

        self.assertEqual(dict_representation["__class__"], base_model.__class__.__name__)
        self.assertEqual(dict_representation["created_at"], base_model.created_at.isoformat())
        self.assertEqual(dict_representation["updated_at"], base_model.updated_at.isoformat())
        self.assertEqual(dict_representation["name"], 'Alice')
        self.assertEqual(dict_representation["my_number"], 123)
    
if __name__ == "__main__":
    unittest.main()
