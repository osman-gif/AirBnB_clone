#!/usr/bin/python3

from unittest import TestCase
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json


class TestFileFileStorage(TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.all_objects = self.storage.all()
        self.base_model = BaseModel()
        self.file_path = self.storage.get_file_path

    def test_all(self):
        self.assertEqual(self.all_objects, FileStorage().get_objects)

        key = '{}.{}'.format(self.base_model.__class__.__name__,
                             self.base_model.id)
        self.assertTrue(self.all_objects[key] == self.base_model)

    def test_reload(self):
        old_dict = self.storage.get_objects.copy()
        self.storage.reload()
        self.assertEqual(old_dict.keys(), self.storage.get_objects.keys())

    def test_save(self):
        self.storage.save()
        with open(self.storage.get_file_path, 'r', encoding="utf-8") as file:
            self.assertEqual(self.storage.get_objects.keys(),
                             json.load(file).keys())

    def test_new(self):
        self.storage.new(self.base_model)
