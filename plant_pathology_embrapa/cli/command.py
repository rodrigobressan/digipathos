class Command():
    def __init__(self,
                 alias: str,
                 command,
                 require_args: bool = False):
        self.alias = alias
        self.command = command
        self.require_args = require_args

    def execute(self, *args):
        if self.require_args:
            return self.command(args)
        else:
            return self.command()
