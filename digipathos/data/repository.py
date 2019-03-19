from abc import ABC, abstractmethod
from typing import List, Dict

import requests

from digipathos import Dataset
from digipathos.constants import ENDPOINT_ITEMS, BASE_URL

class DigipathosRepository(ABC):
    def __init__(self, lang: str = 'pt'):
        self.__items = {}
        self.__crops = {}
        self.lang = lang

    @abstractmethod
    def load_datasets(self) -> List[Dataset]:
        raise NotImplementedError("You should override the method get_items")

    def load_crops(self) -> Dict[str, Dataset]:
        if not self.__items:
            self.__items = self.load_datasets()

        crops = {}

        for item_id, dataset in self.__items.items():
            crop_name = dataset.get_crop_name(lang=self.lang)
            if crop_name not in crops:
                crops[crop_name] = [dataset]
            else:
                crops[crop_name].append(dataset)

        self.__crops = crops

        return crops

    def load_items_from_crop(self, crop_name: str):
        if not self.__items:
            self.__items = self.load_datasets()

        if not self.__crops:
            self.__crops = self.load_crops()

        if crop_name not in self.__crops:
            raise ValueError("Crop name %s is not present on crop list" % crop_name)

        return self.__crops[crop_name]

    def load_item(self, item_id: int) -> Dataset:
        if not self.__items:
            self.__items = self.load_datasets()

        return self.__items[item_id]


class DigipathosRemoteApi(DigipathosRepository):
    def load_datasets(self) -> List[Dataset]:
        url = BASE_URL + ENDPOINT_ITEMS
        resp = requests.get(url=url)
        data = resp.json()

        json_items = data['bitstreams']
        items = {}

        for item in json_items:
            item = Dataset.make_from_json_dict(item)
            item_id = item.get_id()

            items[item_id] = item

        self.__items = items

        return items


class DigipathosMockedApi(DigipathosRepository):
    def load_datasets(self):
        pass
