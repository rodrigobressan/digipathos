import unittest

from plant_pathology_embrapa.constants import BASE_URL
from plant_pathology_embrapa.dataset import Dataset


class TestDataset(unittest.TestCase):
    def setUp(self):
        self.dataset = Dataset(full_name='Abacaxi (Pineapple) - Broca (Pineapple Fruit Borer) - 1.zip',
                               url='/jspui/bitstream/123456789/871/4/Abacaxi%20%28Pineapple%29%20-%20Broca%20%28Pineapple%20Fruit%20Borer%29%20-%201.zip',
                               format='zip',
                               size=1000)

    def test_name_english(self):
        expected_name = 'Pineapple'
        self.assertEqual(self.dataset.get_crop_name(), expected_name)

    def test_name_portuguese(self):
        expected_name = 'Abacaxi'
        self.assertEqual(self.dataset.get_crop_name(lang='pt'), expected_name)

    def test_name_invalid_lang(self):
        ex = 'cz'
        self.assertRaises(ValueError, self.dataset.get_crop_name, lang=ex)

    def test_disorder_invalid_lang(self):
        lang = 'cz'
        self.assertRaises(ValueError, self.dataset.get_disorder_name, lang=lang)

    def test_disorder_english(self):
        expected_disorder = 'Pineapple Fruit Borer'
        self.assertTrue(self.dataset.get_disorder_name(), expected_disorder)

    def test_disorder_portuguese(self):
        expected_disorder = 'Brota'
        self.assertTrue(self.dataset.get_disorder_name(lang='pt'), expected_disorder)

    def test_id(self):
        expected_id = 871
        self.assertEqual(self.dataset.get_id(), expected_id)

    def test_init_from_json(self):
        item = {}
        item[
            'bsLink'] = '/jspui/bitstream/123456789/871/4/Abacaxi%20%28Pineapple%29%20-%20Broca%20%28Pineapple%20Fruit%20Borer%29%20-%201.zip'
        item['name'] = 'Abacaxi (Pineapple) - Broca (Pineapple Fruit Borer) - 1.zip'
        item['format'] = 'zip'
        item['size'] = 1000

        full_url = BASE_URL + item['bsLink']
        other_dataset = Dataset.make_from_json_dict(item=item)

        self.assertEqual(other_dataset.url, full_url)
        self.assertEqual(other_dataset.full_name, item['name'])
        self.assertEqual(other_dataset.extension, item['format'])
        self.assertEqual(other_dataset.size, item['size'])
