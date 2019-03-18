import os
import urllib

from plant_pathology_embrapa import Dataset


def download_dataset(dataset: Dataset, output_dir: str, verbose=True) -> None:
    """
    This method is used to download a given dataset into the disk.
    :param dataset: The dataset object to be persisted into the disk
    :param output_dir: Where the file should be stored
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, "%s.%s" % (dataset.id, dataset.extension.lower()))

    if verbose:
        print('Starting download.. This may take a while to finish. Your download will be ready at: %s ' % file_path)

    urllib.request.urlretrieve(dataset.url, file_path)
