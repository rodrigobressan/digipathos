from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict

import requests

from digipathos.constants import BASE_URL, ENDPOINT_ITEMS
from digipathos.data.dataset import Dataset


class DigipathosRepository(ABC):
    def __init__(self, lang: str = 'pt'):
        self.__items = {}
        self.__crops = {}
        self.lang = lang
        self.last_time_fetched = None

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
    THRESHOLD_CACHE = 10

    def load_datasets(self) -> List[Dataset]:

        if self.last_time_fetched:
            interval = datetime.now() - self.last_time_fetched

            if interval.seconds > self.THRESHOLD_CACHE:
                self.__items = self.fetch_data_from_remote()
        else:  # first time
            self.__items = self.fetch_data_from_remote()

        self.last_time_fetched = datetime.now()

        return self.__items

    def fetch_data_from_remote(self) -> List[Dataset]:
        url = BASE_URL + ENDPOINT_ITEMS
        resp = requests.get(url=url)
        data = resp.json()

        json_items = data['bitstreams']
        items = {}

        for item in json_items:
            item = Dataset.make_from_json_dict(item)
            item_id = item.get_id()

            items[item_id] = item

        return items


class DigipathosMockedApi(DigipathosRepository):
    def load_datasets(self):
        pass
