import unittest

import requests

from plant_pathology_embrapa.data_loader import DataLoader


class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.data_loader = DataLoader()

    def test_load_items(self):
        items = self.data_loader.get_datasets()
        self.assertIsNotNone(items)

    def test_load_crops(self):
        families = self.data_loader.get_crops()
        self.assertIsNotNone(families)

    def test_load_datasets_from_crop(self):
        families = self.data_loader.get_datasets_from_crop('Pineapple')
        self.assertIsNotNone(families)
