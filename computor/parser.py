from computor.tree import Node


class Token(Node):
    OPERATORS = (
        '=',
        '*',
        '+',
        '-',
        '/',
        '%',
    )
    SEPARATORS = (
        '(',
        ')'
    )

    def __init__(self, value, parent=None, left=None, right=None):
        super().__init__(parent, left, right)
        self._value = value

    def __repr__(self):
        return "<Token '%s'>" % self._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def tostr(self):
        return "Token: %s" % self.value


class Parser:
    SEPARATORS = Token.OPERATORS
    PRIORITIES = [
        '+',
        '-',
        '*',
    ]

    def __init__(self):
        pass

    def _lex(self, line):
        tokens = []
        current = ""
        for c in filter(lambda x: not x.isspace(), line):
            if c in Parser.SEPARATORS:
                tokens.append(current)
                tokens.append(c)
                current = ""
            else:
                current += c
        tokens.append(current)
        return tokens

    def _parse(self, tokens):
        if len(tokens) == 1:
            return Token(tokens[0])
        for operator in Parser.PRIORITIES:
            if operator in tokens:
                sep = tokens.index(operator)
                value = tokens.pop(sep)
                return Token(value,
                             None,
                             self._parse(tokens[:sep]),
                             self._parse(tokens[sep:]))

    def parse_line(self, line):
        tokens = self._lex(line)
        print(tokens)
        command = self._parse(tokens)
        return command
