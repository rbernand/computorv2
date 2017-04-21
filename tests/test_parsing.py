from computor.parser import Token, Parser


import logging


log = logging.getLogger('coùmputor')
log.setLevel(logging.DEBUG)


def test_basics():
    parser = Parser()
    a = Token('+', Token('1'), Token('1'))
    assert a == parser.parse_line('1 + 1')
    a = Token('+', Token('2'), Token('3'))
    assert a == parser.parse_line('2 + 3')
    a = Token('+', Token('2'), Token('3'))
    assert a == parser.parse_line('3 + 2')
