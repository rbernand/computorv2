from computor import commands
from computor.commands import COMMANDS


def test_basics():
    assert '/variables' in COMMANDS
    assert COMMANDS['/variables'] == commands.PrintVariables


def test_print_variables():
    pass
