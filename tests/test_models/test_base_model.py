
import unittest
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch
import json
import os


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        del self.base_model

    def test_init(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        cls = 'BaseModel'
        id = self.base_model.id
        expected_str = f"[{cls}] ({id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    def test_save(self):
        with patch('models.storage.save') as mock_save:
            self.base_model.save()
            mock_save.assert_called_once()

    def test_to_dict(self):
        expected_dict = {
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(self.base_model.to_dict(), expected_dict)

    def test_save_and_reload(self):
        # Save the BaseModel to a temporary file
        temp_filename = 'temp.json'
        with patch('models.storage._FileStorage__file_path', temp_filename):
            self.base_model.save()

        # Reload the BaseModel from the saved file
        with patch('models.storage._FileStorage__file_path', temp_filename):
            with open(temp_filename, 'r') as file:
                saved_data = json.load(file)

        # Ensure the reloaded BaseModel has the same attributes
        reloaded_model = BaseModel(**saved_data)
        self.assertEqual(self.base_model.id, reloaded_model.id)
        self.assertEqual(self.base_model.created_at, reloaded_model.created_at)
        self.assertEqual(self.base_model.updated_at, reloaded_model.updated_at)

        # Clean up the temporary file
        os.remove(temp_filename)


if __name__ == '__main__':
    unittest.main()
