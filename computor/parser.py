from computor.tree import Node


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

    def __eq__(self, rhs):
        return self.value == rhs.value


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

    def _lex(self, line, iter_=None):
        print(line)
        tokens = []
        current = ""
        line_ = iter(line)
        for i, c in enumerate(line_):
            if iter_:
                next(iter_)
            if c.isspace():
                continue
            if c == ')':
                break
            if c == '(':
                tokens.append(self._lex(line[i + 1:], line_))
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
                                 None,
                                 self._parse(tokens[:sep]),
                                 self._parse(tokens[sep:]))

    def parse_line(self, line):
        tokens = self._lex(line)
        if '=' in tokens:
            sep = tokens.index('=')
            del(tokens[sep])
            var = tokens[:sep]
            tokens = tokens[sep:]
            print(var)
        print(tokens)
        command = self._parse(tokens)
        return command
