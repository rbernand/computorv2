import logging
from docopt import docopt

import computor
from computor import LOG
from computor.executor import Executor
from computor.commands import COMMANDS
from computor import exceptions

from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.history import FileHistory



DOC = """ComputorV2

Usage:
    computorv2 [-vd] [-i <input_file>]

-h --help     show ths help message
-i <file>     read input from file
-v            verbose mode [default: False]
-d            debug mode [default False]
--version     show version
"""


def prompt_command():
    completer = WordCompleter(COMMANDS.keys())
    return prompt(">>> ",
                  history=FileHistory('.computor_history'),
                  completer=completer)


def set_log_level(verbose, debug):
    if verbose:
        LOG.setLevel(logging.INFO)
        LOG.info("Start computorv2")
    if debug:
        LOG.propagate = False
        stream_handler = logging.StreamHandler()
        fmt = '%(filename)15s:%(lineno)-3d \033[1m%(levelname)-7s\033[0m %(message)s'
        formatter = logging.Formatter(fmt)
        stream_handler.setFormatter(formatter)
        LOG.addHandler(stream_handler)
        LOG.setLevel(logging.DEBUG)
        LOG.debug("Start computorv2 in debug mode")


def main_loop():
    for line in iter(prompt_command, 'exit'):
        LOG.info('Command: %s', line)
        try:
            executor = Executor(line)
            executor.run()
            from computor import variables
        except SyntaxError as err:
            print("invalid command: '%s'" % line)
            print("Reason: '%s'" % err)
        except exceptions.ComputorUnknownCommandError as err:
            print(err)
#        LOG.debug('Tree display:\n%s\n%s\n%s', '_' * 30, root.tostr(), '-' * 30)


def main():
    opts = docopt(DOC, version=computor.__version__)
    set_log_level(opts['-v'], opts['-d'])
    try:
        main_loop()
    except (EOFError, KeyboardInterrupt):
        print('exit')


if __name__ == '__main__':
    main()
