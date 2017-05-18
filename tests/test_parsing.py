from computor.parser import Token, Parser


import logging


log = logging.getLogger('coùmputor')
log.setLevel(logging.DEBUG)


def test_basics():
    parser = Parser()
    a = Token('+', Token('1'), Token('1'))
    assert a == parser.parse_calculation('1 + 1')
    a = Token('+', Token('2'), Token('3'))
    assert a == parser.parse_calculation('2 + 3')
    a = Token('+', Token('2'), Token('3'))
    assert a == parser.parse_calculation('3 + 2')
    a = Token('+',
              Token('2'),
              Token('+',
                    Token('3'),
                    Token('4')))
    assert a == parser.parse_calculation('2 + 3 + 4')
    assert not a == parser.parse_calculation('2 + 3')


def test_priority():
    parser = Parser()
    a = Token('+',
              Token('2'),
              Token('*',
                    Token('3'),
                    Token('4')))
    assert a == parser.parse_calculation('2+ 3 * 4')


def test_parenthesis():
    parser = Parser()
    a = Token('*',
              Token('2'),
              Token('+',
                    Token('3'),
                    Token('4')))
    assert a == parser.parse_calculation('2 * (3 + 4)')
    a = Token('*',
              Token('-',
                    Token('1'),
                    Token('2')),
              Token('/',
                    Token('3'),
                    Token('+',
                          Token('4'),
                          Token('5'))))
    assert a == parser.parse_calculation('(1 - 2) * (3 / (4 + 5))')
