import re

from computor import LOG
from computor.exceptions import ComputorSyntaxError
from computor.tokens import Token, Variable, Function


class Parser:
    SEPARATORS = Token.OPERATORS + ('(', ')')
    REGEX_FUNCTION = re.compile(r'^(?!i)([a-zA-Z]+)\((?!i)([a-zA-Z]+)\)$')
    REGEX_VARIABLE = re.compile(r'^(?!i)([a-zA-Z]+)$')
    PRIORITIES = [
        '+',
        '-',
        '*',
        '/',
        '^',
    ]

    def __init__(self):
        pass

    def lex_line(self, line):
        matrix_depth = 0
        tokens = []
        current = ""
        for char in line:
            if char == '[':
                matrix_depth += 1
            elif char == ']':
                matrix_depth -= 1
            if matrix_depth > 0:
                current += char
                continue
            if char.isspace():
                continue
            if char == ')':
                break
            if char == '(':
                tokens.append(self.lex_line(line))
                continue
            if char in Parser.SEPARATORS:
                if current:
                    tokens.append(current)
                tokens.append(char)
                current = ""
            else:
                current += char
        if current:
            tokens.append(current)
        return tokens

    def _parse(self, tokens):
        if len(tokens) == 1:
            if isinstance(tokens[0], list):
                return self._parse(tokens[0])
            return Token.factory(tokens[0])
        if tokens == []:
            return
        else:
            for operator in Parser.PRIORITIES:
                if operator in tokens:
                    sep = tokens.index(operator)
                    value = tokens.pop(sep)
                    return Token.factory(
                        value,
                        self._parse(tokens[:sep]),
                        self._parse(tokens[sep:]))

    def parse_calculation(self, line):
        tokens = self.lex_line(iter(line))
        return self._parse(tokens)

    def parse_var_or_func(self, line):
        try:
            funcname, varname = self.REGEX_FUNCTION.match(line).groups()
            return Function(funcname, varname)
        except AttributeError:
            LOG.debug('"%s" is not a funtion name', line)
        try:
            varname, = self.REGEX_VARIABLE.match(line).groups()
            return Variable(line)
        except AttributeError:
            raise ComputorSyntaxError('"%s" is neither a valid var name or func name.' % line)

    def parse_input(self, line):
        if '=' in line:
            try:
                left, right = line.split('=')
                if right == '?':
                    left, right = None, left
                else:
                    return self.parse_var_or_func(left), self.parse_calculation(right)
            except ValueError:
                raise ComputorSyntaxError("Too many '='")
        return None, self.parse_calculation(line)
