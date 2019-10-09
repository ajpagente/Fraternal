from commands.command import Command

class ShowCommand(Command):

    def __init__(self, args):
        Command.__init__(self, args)

    def execute(self):
        print("Show me")        