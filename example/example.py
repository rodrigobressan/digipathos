import random

from digipathos.data.data_loader import DataLoader

if __name__ == '__main__':
    data_loader = DataLoader(artifacts_path='artifacts')

    datasets = data_loader.get_datasets()

    crops = data_loader.get_crops()

    datasets_from_crop = data_loader.get_datasets_from_crop('Pineapple')

    # Not let's download a dataset
    dataset_id = random.choice(list(datasets.keys()))
    data_loader.download_dataset(dataset_id=dataset_id)

    data_loader.download_datasets_from_crop('Pineapple')
    data_loader.download_all_datasets()