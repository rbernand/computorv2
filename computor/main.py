from docopt import docopt
import logging

import computor
from computor import log

from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory

from computor.parser import Parser


__doc__ = """ComputorV2

Usage:
    computorv2 [-vd] [-i <input_file>]

-h --help     show ths help message
-i <file>     read input from file
-v            verbose mode [default: False]
-d            debug mode [default False]
--version     show version
"""


def prompt_command():
    return prompt(">>> ", history=FileHistory('.computor_history'))


def set_log_level(verbose, debug):
    if verbose:
        log.setLevel(logging.INFO)
        log.info("Start computorv2")
    if debug:
        log.propagate = False
        sh = logging.StreamHandler()
        fmt = '%(filename)15s:%(lineno)-3d \033[1m%(levelname)-7s\033[0m %(message)s'
        formatter = logging.Formatter(fmt)
        sh.setFormatter(formatter)
        log.addHandler(sh)
        log.setLevel(logging.DEBUG)
        log.debug("Start computorv2 in debug mode")


def main_loop():
    parser = Parser()
    for line in filter(bool, iter(prompt_command, 'exit')):
        log.info('Command: %s', line)
        root = parser.parse_computation(line)
        print(root())
        log.debug('Tree display:\n%s\n%s\n%s', '_' * 30, root.tostr(), '-' * 30)


def main():
    opts = docopt(__doc__, version=computor.__version__)
    set_log_level(opts['-v'], opts['-d'])
    try:
        main_loop()
    except (EOFError, KeyboardInterrupt):
        print('exit')


if __name__ == '__main__':
    main()
