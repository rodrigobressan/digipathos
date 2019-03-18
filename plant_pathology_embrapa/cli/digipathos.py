from plant_pathology_embrapa.cli.commands.command import Command, get_commands, transpose_and_print
from plant_pathology_embrapa.data_loader import DataLoader

# print('[1] list_datasets')
# print('[2] list_crops')
# print('[3] list_datasets_from_crop')
# print('[4] get_dataset')
# print('[5] download_dataset')
# print('[6] download_all_datasets')
# print('[7] download_datasets_from_crop')
#
DEFAULT_LANGUAGE = 'en'

data_loader = DataLoader(auto_fetch=False, lang=DEFAULT_LANGUAGE)
commands = get_commands(data_loader)


def print_header():
    header = """  
    ____  _       _             __  __              
   / __ \(_)___ _(_)___  ____ _/ /_/ /_  ____  _____
  / / / / / __ `/ / __ \/ __ `/ __/ __ \/ __ \/ ___/
 / /_/ / / /_/ / / /_/ / /_/ / /_/ / / / /_/ (__  ) 
/_____/_/\__, /_/ .___/\__,_/\__/_/ /_/\____/____/  
        /____/ /_/                                  """

    print(header)


def init_interactive_mode():
    while True:
        try:
            print_header()
            command = read_command()
            if command.require_args:
                arg = input('%s: ' % command.args_description)

                if arg:
                    run_command_with_argument(command, arg)
                else:
                    print('You should provide an argument for this command')
            else:
                command.execute()
        except Exception:
            print("You should select a valid option from the command list")


def run_command_with_argument(command, arg):
    try:
        command.execute(arg)
    except Exception as e:
        print('There was an error on your command. Make sure your input is correct. Exception: ', e)


def read_command() -> Command:
    command_ids = ['ID']
    command_names = ['Command']
    for id, command in commands.items():
        command_ids.append(id)
        command_names.append(command.desc)

    commands_list = [command_ids, command_names]

    transpose_and_print(commands_list)

    try:
        command_id = int(input('Command: '))
        command = commands[command_id]
        return command
    except Exception:
        raise Exception()


if __name__ == '__main__':
    init_interactive_mode()
