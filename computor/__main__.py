import re
import logging
from docopt import docopt
from functools import partial

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


def prompt_command(prompt_string=">>> "):
    completer = WordCompleter(COMMANDS.keys())
    prompt_line = partial(prompt,
                          prompt_string,
                          history=FileHistory('.computor_history'),
                          completer=completer,
                          complete_while_typing=False,
                          enable_history_search=True,)
    for line in iter(prompt_line, 'exit'):
        yield line


def _iter_file(filename):
    with open(filename, 'r') as source:
        for line in source.readlines():
            if line.startswith('#'):
                LOG.warning('Comment %s', line)
                continue
            yield line


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


def _clear_line(line):
    cleaner = re.compile(r'\s')
    return cleaner.sub('', line)


def main_loop(input_method=prompt_command):
    for line in filter(bool, map(_clear_line ,input_method())):
        LOG.info('Command: %s', line)
        try:
            executor = Executor(line)
            executor.run()
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
        if opts['-i']:
            main_loop(partial(_iter_file, opts['-i']))
        else:
            main_loop()
    except (EOFError, KeyboardInterrupt):
        print('exit')


if __name__ == '__main__':
    main()
