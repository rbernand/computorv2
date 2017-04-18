from docopt import docopt
import logging

import computor
from computor import log
from prompt_toolkit import prompt
from computor.parser import Parser


__doc__ = """ComputorV2

Usage:
    computorv2 [-vd] [<input_file>]

-h --help     show ths help message
-v            verbose mode [default: False]
-d            debug mode [default False]
--version  show version
"""


def prompt_command():
    print('>>> ', end='')
    return prompt()


def main():
    opts = docopt(__doc__, version=computor.__version__)
    if opts['-v']:
        log.setLevel(logging.INFO)
        log.info("Start computorv2")
    if opts['-d']:
        log.setLevel(logging.DEBUG)
        log.info("Start computorv2 in debug mode")
    parser = Parser()
    try:
        for line in iter(prompt_command, ''):
            root = parser.parse_line(line)
            root.print_tree()
    except (EOFError, KeyboardInterrupt):
        print('exit')


if __name__ == '__main__':
    main()
