<img width=75% src="docs/figs/logo.png">

[![PyPI version](https://badge.fury.io/py/digipathos.svg)](https://pypi.org/project/digipathos)
[![Build Status](https://travis-ci.org/bresan/digipathos_plant_pathology.svg?branch=master)](https://travis-ci.org/bresan/digipathos_plant_pathology)
[![codecov](https://codecov.io/gh/bresan/digipathos_plant_pathology/branch/master/graph/badge.svg)](https://codecov.io/gh/bresan/digipathos_plant_pathology)
[![GitHub](https://img.shields.io/github/license/bresan/digipathos_plant_pathology.svg)](https://github.com/bresan/digipathos_plant_pathology/blob/master/LICENSE.md)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e02bc243822c4ce884c4adf87ff6e9f7)](https://www.codacy.com/app/bresan/digipathos_plant_pathology?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=bresan/digipathos_plant_pathology&amp;utm_campaign=Badge_Grade)

# Overview

This project is aimed to serve as a wrapper for the Digipathos dataset, in order to list and download public data from plant pathologies provided by Embrapa (Brazilian Agricultural Research Corporation).

# Installation

The installation is pretty simple if you have a virtualenv already installed on your machine. If you don't please rely to [VirtualEnv official documentation](https://virtualenv.pypa.io/en/latest/).

```bash
pip install digipathos
```

# Documentation

Besides the docstrings, major details about the documentation can be found [here](https://.readthedocs.io/en/latest/).

# Testing

This project is inteded to suit most of the existent needs, so for this reason, testability is a major concern. Most of the code is heavily tested, along with [Travis](https://travis-ci.org/bresan/digipathos_plant_pathology) as Continuous Integration tool to run all the unit tests once there is a new commit.

# Usage

You can use Digipathos in two different ways: via terminal or programatically.

## CLI (Command-Line Interface)

This mode is highly recommended for those who are looking to explore a little bit the dataset. Here you can do the same operations from the programmatic mode, but with the advantage of being able to see all the data that is being retrieved.


```bash
python browser.py
```

And then you're gonna be greeted by our dataset browser :-)

<p align="center"><img width=75% src="docs/figs/browser.png"></p>

An example listing all the datasets:

<p align="center"><img width=75% src="docs/figs/datasets.png"></p>


## Programmatically


```python
data_loader = DataLoader()

# list all the datasets
datasets = data_loader.get_datasets()

# now lets give a look at the crops
crops = data_loader.get_crops()

# how about getting all the datasets from a crop?
datasets_from_crop = data_loader.get_datasets_from_crop('Pineapple')

# now let's download a random dataset
dataset_id = random.choice(list(datasets.keys()))
data_loader.download_dataset(dataset_id=dataset_id)

# download all from a given crop
data_loader.download_datasets_from_crop('Pineapple')

# download all the datasets
data_loader.download_all_datasets()
```

Pretty simple, huh?

A working example can be found [here as a Python script](https://github.com/bresan/digipathos_plant_pathology/blob/master/example/example.py).


# Troubleshooting

In case of any issue with the project, or for further questions, do not hesitate to open an issue here on GitHub.

# Contributions

Contributions are really welcome, so feel free to open a pull request :-)