#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBase(unittest.TestCase):
    
    def setUp(self):
        self.base_model = BaseModel()
        self.id = self.base_model.id
        self.created_at = self.base_model.created_at
        self.updated_at = self.base_model.updated_at
        
    
    def test_init(self):
        self.assertIsNotNone(self.id, int)
        self.assertIsNotNone(self.created_at, int)
        self.assertIsNotNone(self.updated_at, int)
    
    def test_save(self):
        self.base_model.save()
        self.assertNotEqual(self.updated_at,self.created_at)
    
    def test_to_dict(self):
        my_dict = self.base_model.to_dict()
        
        self.assertIn('id', my_dict)
        self.assertIn('created_at', my_dict)
        self.assertIn('updated_at', my_dict)
        self.assertIn('__class__', my_dict)
