import random

from plant_pathology_embrapa.data_loader import DataLoader

if __name__ == '__main__':
    data_loader = DataLoader(artifacts_path='artifacts')

    datasets = data_loader.get_datasets()
    print('Datasets: ', datasets)

    crops = data_loader.get_crops()
    print('Crops: ', crops)

    datasets_from_crop = data_loader.get_datasets_from_crop('Pineapple')
    print('Datasets from crop: ', datasets_from_crop)

    # Not let's download a dataset
    dataset_id = random.choice(list(datasets.keys()))
    data_loader.download_dataset(dataset_id=dataset_id)
    print('Download done')
