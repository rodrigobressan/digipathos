import os
from typing import List, Dict

from digipathos.data.dataset import Dataset
from digipathos.data.repository import DigipathosRemoteApi
from digipathos.utils import download_utils


class DataLoader:
    """
    This class should be used to load data from the Digipathos API
    """

    def __init__(self,
                 artifacts_path: str = 'artifacts',
                 lang: str = 'en',
                 auto_fetch=True):
        """
        DataLoader basic initializer
        :param artifacts_path: where the artifacts will be stored after downloaded
        :param lang: the language to be used to fetch names (crops and disorders)
        :param auto_fetch: should data be fetched automatically on initialization
        :param repository: the repository to be used. You can replace it here for another DataSource, but it must be a
        child of DigitpathosRepository
        """
        self.artifacts_path = artifacts_path
        self.lang = lang
        self.repository = DigipathosRemoteApi(self.lang)

        if auto_fetch:
            self.items = self.repository.load_datasets()
            self.crops = self.repository.load_crops()

    def get_datasets(self) -> List[Dataset]:
        """
        Used to get all the datasets without downloading them. In case you are looking
        to download, please refer to the download_all_datasets method.
        :return: a List containing all the available datasets
        """
        return self.repository.load_datasets()

    def get_crops(self) -> Dict[str, Dataset]:
        """
        Used to get all the crops without downloading them
        :return: a dictionary containing all the datasets
        """
        return self.repository.load_crops()

    def get_datasets_from_crop(self, crop_name: str) -> List[Dataset]:
        """
        Used to get the list of all datasets related to a given crop without downloading them. In case you are looking
        to download, please refer to the download_datasets_from_crop method.
        :param crop_name: the name of the crop
        :return: a List containing all the Datasets from a given crop
        """
        return self.repository.load_items_from_crop(crop_name)

    def get_dataset(self, dataset_id: int) -> Dataset:
        """
        Used to get the information about a given dataset without downloading it. In case you are looking to download,
        please refer to the download_dataset method.
        :param dataset_id: the dataset id
        :return: a Dataset object containing the dataset
        """
        return self.repository.load_item(dataset_id)

    def download_dataset(self, dataset_id: int) -> None:
        """
        Used to download a given dataset to the disk
        :param dataset_id: the id of the dataset
        """
        item = self.repository.load_item(dataset_id)
        download_utils.download_dataset(item, self.artifacts_path)

    def download_all_datasets(self) -> None:
        """
        Used to download all the datasets
        """
        datasets = self.repository.load_datasets()

        for dataset in datasets:
            download_utils.download_dataset(dataset, self.artifacts_path)

    def download_datasets_from_crop(self, crop_name: str) -> None:
        """
        Used to download all the datasets from a given crop name. This method will output the download crops into a new
        folder with the same name as the crop. e.g.: /artifacts/<crop_name>
        :param crop_name: the name of the crop
        """
        items = self.repository.load_items_from_crop(crop_name)

        output_path = os.path.join(self.artifacts_path, crop_name)

        for item in items:
            download_utils.download_dataset(item, output_path)
