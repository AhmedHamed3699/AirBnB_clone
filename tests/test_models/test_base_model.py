#!/usr/bin/python3
"""This module is for testing BaseModel."""
import unittest
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """A class for testing base model."""

    def test_creation_with_arguments(self):
        """Test creating a BaseModel with arguments."""
        data = {
            'id': '123',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-01T12:30:00.000000',
        }

        with patch('uuid.uuid4', return_value='123'):
            obj = BaseModel(**data)

        self.assertEqual(obj.id, '123')
        self.assertEqual(obj.created_at, datetime(2022, 1, 1, 12, 0, 0))
        self.assertEqual(obj.updated_at, datetime(2022, 1, 1, 12, 30, 0))

    def test_creation_without_arguments(self):
        """Test creating a BaseModel without arguments."""
        with patch('uuid.uuid4', return_value='123'):
            obj = BaseModel()

        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_save_method(self):
        """Test the save method."""
        obj = BaseModel()

        with patch('models.storage.save') as mock_save:
            obj.save()

        mock_save.assert_called_once()

    def test_to_dict_method(self):
        """Test the to_dict method."""
        obj = BaseModel()

        expected_dict = {
            'id': obj.id,
            '__class__': 'BaseModel',
            'created_at': obj.created_at.isoformat(),
            'updated_at': obj.updated_at.isoformat(),
        }

        self.assertEqual(obj.to_dict(), expected_dict)

    def test_str_method(self):
        """Test the __str__ method."""
        obj = BaseModel()

        expected_str = f"[BaseModel] ({obj.id}) {obj.__dict__}"

        self.assertEqual(str(obj), expected_str)


if __name__ == '__main__':
    unittest.main()
