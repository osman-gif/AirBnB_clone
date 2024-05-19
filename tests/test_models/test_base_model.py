#!/usr/bin/python3
"""
This file tests the functionality of the base_model module
"""
from unittest import TestCase
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(TestCase):

    def setUp(self):
        self.baseModel = BaseModel()
        self.baseModel.name = 'osman'
        self.baseModel_dict = self.baseModel.to_dict()
        self.recreated_base_model = BaseModel(**self.baseModel_dict)
        self.recreated_base_model_dict = self.recreated_base_model.to_dict()

    def test_id_is_set(self):
        self.assertIsInstance(self.baseModel.id, str)

    def test_updated_at_is_set(self):
        self.assertIsInstance(self.baseModel.updated_at, datetime)

    def test_created_at_is_set(self):
        self.assertIsInstance(self.baseModel.created_at, datetime)

    def test__str__(self):
        expected_output = '[{}] ({})'.format(self.baseModel.__class__.__name__,
                                             self.baseModel.id)
        self.assertEqual(self.baseModel.__str__().split(' ')[0:2],
                         expected_output.split(' ')[0:2])

    def test_save(self):
        old_date = self.baseModel.updated_at
        updated_date = self.baseModel.save()

        self.assertNotEqual(old_date, updated_date)

    def test_to_dict(self):
        for k, v in self.baseModel_dict.items():
            if k == 'created_at':
                self.assertEqual(datetime.fromisoformat(v),
                                 self.baseModel.created_at)
            elif k == 'id':
                self.assertEqual(v, str(self.baseModel.id))

    def test_object_recreation(self):
        print(self.baseModel_dict, '\n', self.recreated_base_model_dict)
        self.assertEqual(self.baseModel_dict, self.recreated_base_model_dict)
        self.assertIsNot(self.baseModel_dict, self.recreated_base_model_dict)
