from computor.tree import Node
from computor import log


class Token(Node):
    OPERATORS = (
        '=',
        '*',
        '+',
        '-',
        '/',
        '%',
        '^'
    )
    SEPARATORS = (
        '(',
        ')'
    )

    def __init__(self, value, left=None, right=None):
        super().__init__(left, right)
        self.value = value

    def __repr__(self):
        return "<Token '%s'>" % self._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __str__(self):
        return "Token: [%s]" % self.value

    def __eq__(self, rhs):
        print(self, rhs)
        return self.value == rhs.value\
            and ((self.left == rhs.left and self.right == rhs.right) or
                 (self.left == rhs.right and self.right == rhs.left))


class Parser:
    SEPARATORS = Token.OPERATORS + ('(', ')')
    PRIORITIES = [
        '+',
        '-',
        '*',
        '/',
        '^',
    ]

    def __init__(self):
        pass

    def _lex(self, line):
        matrix_depth = 0
        tokens = []
        current = ""
        for i, c in enumerate(line):
            if c == '[':
                matrix_depth += 1
            elif c == ']':
                matrix_depth -= 1
            if matrix_depth > 0:
                current += c
                continue
            if c.isspace():
                continue
            if c == ')':
                break
            if c == '(':
                tokens.append(self._lex(line))
                continue
            if c in Parser.SEPARATORS:
                if current:
                    tokens.append(current)
                tokens.append(c)
                current = ""
            else:
                current += c
        if current:
            tokens.append(current)
        return tokens

    def _parse(self, tokens):
        if len(tokens) == 1:
            if isinstance(tokens[0], list):
                return self._parse(tokens[0])
            return Token(tokens[0])
        if len(tokens) == 0:
            return
        else:
            for operator in Parser.PRIORITIES:
                if operator in tokens:
                    sep = tokens.index(operator)
                    value = tokens.pop(sep)
                    return Token(value,
                                 self._parse(tokens[:sep]),
                                 self._parse(tokens[sep:]))

    def parse_line(self, line):
        tokens = self._lex(iter(line))
        log.debug('tokens: %s', tokens)
        if '=' in tokens:
            sep = tokens.index('=')
            del(tokens[sep])
            var = tokens[:sep]
            tokens = tokens[sep:]
        command = self._parse(tokens)
        return command
