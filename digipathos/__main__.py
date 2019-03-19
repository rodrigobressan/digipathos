from digipathos.cli.browser import init_interactive_mode


def main():
    init_interactive_mode()

    print('called main')


if __name__ == '__main__':
    init_interactive_mode()
    print('Browser called!')
