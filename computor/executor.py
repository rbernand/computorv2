from enum import Enum

from computor import LOG, variables, functions
from computor.parser import Parser
from computor.tokens import Token, Variable, Function
from computor.exceptions import ComputorError, ComputorUnknownCommandError
from computor.commands import COMMANDS


class Executor:
    class Type(Enum):
        ASSIGNATION = 1
        CALCULATION = 2
        COMMAND = 3

    def __init__(self, line):
        self._left = None
        self._right = None
        self._cmd = None
        if line.startswith('/'):
            try:
                cmd, *attrs = line.split()
                self._cmd = COMMANDS[cmd](*attrs)
            except KeyError:
                raise ComputorUnknownCommandError(line[1:])
        else:
            parser = Parser()
            self._left, self._right = parser.parse_input(line)

    def is_assignation(self):
        return isinstance(self._left, (Variable, Function)) \
            and isinstance(self._right, Token)

    def is_calculation(self):
        return self._left is None and isinstance(self._right, Token)

    def is_command(self):
        return self._cmd is not None \
            and self._left is None and self._right is None

    @property
    def type(self):
        if self.is_assignation():
            return self.Type.ASSIGNATION
        elif self.is_calculation():
            return self.Type.CALCULATION
        elif self.is_command():
            return self.Type.COMMAND
        else:
            raise NotImplementedError("Cannot determinate type")

    def run(self):
        actions = {
            self.Type.ASSIGNATION: self.execute_assignation,
            self.Type.CALCULATION: self.execute_calculation,
            self.Type.COMMAND: self.execute_command,
        }
        try:
            actions[self.type]()
        except ComputorError as err:
            print(err)

    def execute_assignation(self):
        destinations = {
            Function: functions,
            Variable: variables
        }
        if isinstance(self._left, Function):
            res = self._left.reduce(self._right)
        else:
            res = self._right()
        LOG.debug('Assigning value: %s to %s %s',
                  res.tostring(),
                  ['variable', 'function'][isinstance(self._left, Function)],
                  self._left.name)
        destinations[self._left.__class__].add(self._left.name, res)

    def execute_calculation(self):
        print(self._right())

    def execute_command(self):
        self._cmd.run()
