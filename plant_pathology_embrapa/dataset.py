import re

from plant_pathology_embrapa.constants import BASE_URL

VALID_LANGUAGES = ['pt', 'en']
pattern_en = '\(([^)]+)\)'
pattern_pt = '(?<!\S)\w+(?!\S)'


class Dataset:
    """
    Used to store all the info from a given dataset
    """

    def __init__(self,
                 full_name: str,
                 url: str,
                 format: str,
                 size: float):
        self.full_name = full_name
        self.extension = format
        self.size = size

        self.url = BASE_URL + url
        self.id = self.get_id()

    @classmethod
    def make_from_json_dict(cls, item: dict):
        """
        Used to create a Dataset object from a json response
        :param item: the json item dict
        :return: a new Dataset object
        """
        return cls(full_name=item['name'],
                   url=item['bsLink'],
                   format=item['format'],
                   size=item['size'])

    def validate_language(self, lang: str):
        """
        Used to validate if the passed lang argument is valid or not. In case it isn't, it will throw a ValueError
        exception
        :param lang: the lang to be validated
        :return: ValueError if language is not valid
        """
        if lang not in VALID_LANGUAGES:
            raise ValueError('You should provide a valid language. Valid languages: %s' % VALID_LANGUAGES)

    def get_crop_name(self, lang: str = 'en'):
        """
        Used to get the crop name from the dataset for a specified language
        :param lang: the language to retrieve the crop name
        :return: the crop name
        """
        self.validate_language(lang)

        if lang == 'en':
            name = self.find(pattern_en, self.full_name, 0)
        elif lang == 'pt':
            name = self.find(pattern_pt, self.full_name, 0)

        return name

    def get_disorder_name(self, lang: str = 'en'):
        """
        Used to get the disorder name from the dataset for a specified language
        :param lang: the language to retrieve the disorder name
        :return: the disorder name
       """
        self.validate_language(lang)

        if lang == 'en':
            name = self.find(pattern_en, self.full_name, 1)
        elif lang == 'pt':
            name = self.find(pattern_pt, self.full_name, 1)

        return name

    def find(self, pattern: str, contents: str, index: int) -> str:
        """
        Used to find a text in a given index based on a RegEx pattern
        :param pattern: the pattern to be searched
        :param contents: the text to be used
        :param index: the index to be fetched
        :return: the located text in the given index that matches the pattern
        """
        try:
            return re.findall(pattern, contents)[index]
        except IndexError:
            return None

    def get_id(self) -> int:
        """
        Used to get the id from a given dataset.
        :return: the id (int)
        """
        id = self.url.split('/')[6]
        return int(id)
