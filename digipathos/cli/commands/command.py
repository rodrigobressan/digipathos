import os
import sys
from abc import ABC, abstractmethod
from typing import Dict, List

from terminaltables import AsciiTable

from digipathos import Dataset, DataLoader


class Command(ABC):
    def __init__(self,
                 desc: str,
                 command,
                 lang: str,
                 require_args: bool = False,
                 args_description: str = None,
                 arg_type=str):
        self.desc = desc
        self.command = command
        self.require_args = require_args
        self.args_description = args_description
        self.arg_type = arg_type
        self.lang = lang

        if args_description:
            self.require_args = True

    def execute(self, *args):
        if self.require_args:
            casted_arg = self.arg_type(args[0])
            self.print_pretty(self.command(casted_arg))
        else:
            self.print_pretty(self.command())

        input('Press Enter to return to the main menu')
        # cls()

    @abstractmethod
    def print_pretty(self, command_response):
        raise NotImplementedError("You should override the method print_pretty")


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class ListDatasets(Command):
    def print_pretty(self, command_response: Dict[str, Dataset]) -> None:
        dataset_ids = ['ID']
        dataset_crops = ['Crop']
        dataset_disorders = ['Disorder']

        for dataset_id, dataset in command_response.items():
            dataset_ids.append(dataset_id)
            dataset_crops.append(dataset.get_crop_name(lang=self.lang))
            dataset_disorders.append(dataset.get_disorder_name(lang=self.lang))

        output = [dataset_ids, dataset_crops, dataset_disorders]
        transpose_and_print(output)


class ListCrops(Command):
    def print_pretty(self, command_response: Dict[str, List[int]]) -> None:
        datasets_crops = ['Crop']
        for name in command_response.keys():
            datasets_crops.append(name)

        output = [datasets_crops]
        transpose_and_print(output)


class ListDatasetsFromCrop(Command):
    def print_pretty(self, command_response: List[Dataset]) -> None:
        dataset_ids = ['ID']
        dataset_disorders = ['Disorder']

        for dataset in command_response:
            dataset_ids.append(dataset.get_id())
            dataset_disorders.append(dataset.get_disorder_name(lang=self.lang))

        output = [dataset_ids, dataset_disorders]
        transpose_and_print(output)


class DownloadDataset(Command):
    def print_pretty(self, command_response):
        pass


class DownloadAllDatasets(Command):
    def print_pretty(self, command_response):
        pass


class DownloadAllDatasetsFromCrop(Command):
    def print_pretty(self, command_response):
        pass


class Exit(Command):
    def print_pretty(self, command_response):
        pass


def transpose_and_print(data: List) -> None:
    output = list(map(list, zip(*data)))
    print(AsciiTable(output).table)


def get_commands(data_loader: DataLoader) -> Dict[int, Command]:
    commands = {
        0: Exit(desc='Exit the application',
                command=sys.exit,
                lang=data_loader.lang),

        1: ListDatasets(desc='List all datasets',
                        command=data_loader.get_datasets,
                        lang=data_loader.lang),

        2: ListCrops(desc='List all crops',
                     command=data_loader.get_crops,
                     lang=data_loader.lang),

        3: ListDatasetsFromCrop(desc='List all datasets from a given crop',
                                command=data_loader.get_datasets_from_crop,
                                require_args=True,
                                args_description='Crop name',
                                lang=data_loader.lang),

        4: DownloadDataset(desc='Download single dataset',
                           command=data_loader.download_dataset,
                           require_args=True,
                           args_description='Dataset id',
                           arg_type=int,
                           lang=data_loader.lang),

        5: DownloadAllDatasets(desc='Download all datasets',
                               command=data_loader.download_all_datasets,
                               lang=data_loader.lang),

        6: DownloadAllDatasetsFromCrop(desc='Download all datasets from a given crop',
                                       command=data_loader.download_datasets_from_crop,
                                       arg_type=str,
                                       args_description='Crop name',
                                       lang=data_loader.lang)
    }

    return commands
