import abc

from computor import variables


class Command(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def command_string(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass


class PrintVariables(Command):
    command_string = '/variables'

    def run(self):
        if variables.VARIABLES:
            leftcol = max(map(len, variables.VARIABLES.keys()))
            for i, (name, value) in enumerate(variables.VARIABLES.items()):
                print("%2d -> %*s = %s" % (i, leftcol, name, value))
        else:
            print('No variables registred in current session')



class PrintFunctions(Command):
    command_string = '/functions'

    def run(self):
        if function.FUNCTIONS:
            leftcol = max(map(len, variables.VARIABLES.keys()))
            for i, (name, value) in enumerate(variables.VARIABLES.items()):
                print("%2d -> %*s = %s" % (i, leftcol, name, value))
        else:
            print('No variables registred in current session')



COMMANDS = {cmd.command_string: cmd for cmd in Command.__subclasses__()}
