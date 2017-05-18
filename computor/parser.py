from computor.tree import Node
from computor import log

#import sys
#sys.setrecursionlimit(70)

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

    @staticmethod
    def factory(value, left=None, right=None):
        if value.isalpha():
            return Variable(value, left, right)
        constructors = {
            '+': Add,
            '-': Sub,
            '*': Mul,
            '/': Div,
            '^': Pow,
        }
        return constructors.get(value, Value)(value, left, right)

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


class Add(Token):
    def __call__(self):
        return self.left() + self.right()


class Sub(Token):
    def __call__(self):
        if self.right is None and self.left:
            return 0 - self.left()
        elif self.left is None and self.right:
            return 0 - self.right()
        else:
            return self.left() - self.right()


class Value(Token):
   def __call__(self):
        try:
            return float(self.value)
        except ValueError:
            if self.value.isalpha():
                try:
                    return Variables.get(self.value)
                except KeyError:
                    log.error("Variable Not found '%s'", self.value)
            else:
                pass  # is imaginary


class Mul(Token):
    def __call__(self):
        return self.left() * self.right()


class Div(Token):
    def __call__(self):
        return self.left() / self.right()


class Pow(Token):
    def __call__(self):
        return self.left() ** self.right()


class Variable(Token):
    instances = set()

    def __call__(self):
        return self.value


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

    def lex_line(self, line):
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
                tokens.append(self.lex_line(line))
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
            return Token.factory(tokens[0])
        if len(tokens) == 0:
            return
        else:
            for operator in Parser.PRIORITIES:
                if operator in tokens:
                    sep = tokens.index(operator)
                    value = tokens.pop(sep)
                    return Token.factory(value,
                                 self._parse(tokens[:sep]),
                                 self._parse(tokens[sep:]))

    def parse_calculation(self, line):
        tokens = self.lex_line(iter(line))
        log.debug('tokens: %s', tokens)
        if '=' in tokens:
            sep = tokens.index('=')
            del(tokens[sep])
            Variables.add(tokens[:sep])
            tokens = tokens[sep:]
        command = self._parse(tokens)
        return command
