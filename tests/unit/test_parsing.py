import pytest

from computor.parser import Parser
from computor.tokens import Token, Variable, Function


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


def test_parse_variable():
    parser = Parser()
    assert isinstance(parser.parse_var_or_func('foo'), Variable)
    assert isinstance(parser.parse_var_or_func('foo(x)'), Function)
    with pytest.raises(SyntaxError): parser.parse_var_or_func('i')
    with pytest.raises(SyntaxError): parser.parse_var_or_func('i(x)')
    with pytest.raises(SyntaxError): parser.parse_var_or_func('i(i)')
    with pytest.raises(SyntaxError): parser.parse_var_or_func('a42')
    with pytest.raises(SyntaxError): parser.parse_var_or_func('42(x)')
    with pytest.raises(SyntaxError): parser.parse_var_or_func('foo(43)')
