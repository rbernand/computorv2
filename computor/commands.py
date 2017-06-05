import os
import abc

from computor import functions, variables


class Command(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def command_string(self):
        pass

    @abc.abstractstaticmethod
    def run():
        pass


class PrintVariables(Command):
    command_string = '/variables'

    @staticmethod
    def run():
        if variables.VARIABLES:
            leftcol = max(map(len, variables.VARIABLES.keys()))
            for i, (name, value) in enumerate(variables.VARIABLES.items()):
                print("%2d -> %*s = %s" % (i, leftcol, name, value))
        else:
            print('No variables registred in current session')


class PrintFunctions(Command):
    command_string = '/functions'

    @staticmethod
    def run():
        if functions.FUNCTIONS:
            leftcol = max(map(len, functions.FUNCTIONS.keys()))
            for i, (name, value) in enumerate(functions.FUNCTIONS.items()):
                print("%2d -> %*s = %s" % (i, leftcol, name, value))
        else:
            print('No functions registred in current session')


class PrintAll(Command):
    command_string = '/all'

    @staticmethod
    def run():
        width, _ = os.get_terminal_size()
        print(" VARIABLES ".center(width, "="))
        PrintVariables.run()
        print(" FUNCTIONS ".center(width, "="))
        PrintFunctions.run()


COMMANDS = {cmd.command_string: cmd for cmd in Command.__subclasses__()}
