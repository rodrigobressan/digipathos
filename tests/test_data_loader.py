import os
import shutil
import unittest
from os.path import exists

from digipathos.data.data_loader import DataLoader


class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.data_loader = DataLoader(lang='pt')

    def test_load_items(self):
        items = self.data_loader.get_datasets()
        self.assertIsNotNone(items)

    def test_load_crops(self):
        families = self.data_loader.get_crops()
        self.assertIsNotNone(families)

    def test_load_datasets_from_crop(self):
        families = self.data_loader.get_datasets_from_crop('Abacaxi')
        self.assertIsNotNone(families)

    def test_load_datasets_from_crop_invalid(self):
        self.assertRaises(ValueError, self.data_loader.get_datasets_from_crop, 'Jacaré')

    def test_get_dataset(self):
        item = self.data_loader.get_dataset(871)
        self.assertIsNotNone(item)

    def test_download_dataset(self):
        self.data_loader.download_dataset(871)

        output = os.path.join(self.data_loader.artifacts_path, '871.zip')
        self.assertTrue(exists(output))

        shutil.rmtree(self.data_loader.artifacts_path)

    def test_download_datasets_from_crop(self):
        self.data_loader.download_datasets_from_crop('Abacaxi')
        output = os.path.join(self.data_loader.artifacts_path, 'Abacaxi')
        count_dirs = len(os.listdir(output))
        self.assertTrue(count_dirs > 1)

        shutil.rmtree(self.data_loader.artifacts_path)
