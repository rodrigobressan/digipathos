import argparse

import sys
print(sys.path)

from plant_pathology_embrapa.cli.command import Command
from plant_pathology_embrapa.data_loader import DataLoader

data_loader = DataLoader(auto_fetch=False)
commands = {
    1: Command('list_datasets', data_loader.get_datasets),
    2: Command('list_crops', data_loader.get_crops),
    3: Command('list_datasets_from_crop', data_loader.get_datasets_from_crop)
}



def init_interactive_mode():
    print('Interactive mode started. Input 0 to exit')

    command = read_command()
    print(command.execute())



def read_command() -> Command:
    print('List of commands: ')

    for id, command in commands.items():
        print('[%d] %s' % (id, command.alias))

    # print('[1] list_datasets')
    # print('[2] list_crops')
    # print('[3] list_datasets_from_crop')
    # print('[4] get_dataset')
    # print('[5] download_dataset')
    # print('[6] download_all_datasets')
    # print('[7] download_datasets_from_crop')
    #
    command_id = int(input('Selected action: '))
    return commands[command_id]


if __name__ == '__main__':

    init_interactive_mode()

    # parser = argparse.ArgumentParser()
    # parser.add_argument("-i", "--interactive", action='count',
    #                     help="increase output verbosity")
    # args = parser.parse_args()
    #
    # if args.interactive:
    #     init_interactive_mode()
