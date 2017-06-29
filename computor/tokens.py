from computor.tree import Node
from computor import variables
from computor import LOG


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
        self._value = None
        self.value = value

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

    def __repr__(self):
        return "<Token '%s'>" % self._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def tostring(self, sep=" "):
        return sep.join(str(x.value) for x in self)

    def __str__(self):
        return "%s: [%s]" % (self.__class__.__name__, self.value)

    def __eq__(self, rhs):
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
        return self.left() - self.right()


class Value(Token):
    def __call__(self):
        try:
            return float(self.value)
        except ValueError:
            if self.value.isalpha():
                try:
                    return variables.get(self.value)
                except KeyError:
                    LOG.error("Variable Not found '%s'", self.value)
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
    def __init__(self, value, left=None, right=None):
        super().__init__(value, left, right)
        self._name = value

    @property
    def name(self):
        return self._name

    def __call__(self):
        return Value(variables.get(self._name))()

    def __hash__(self):
        return hash(self._name)


class Function(Token):
    def __init__(self, name, varname, left=None, right=None):
        super().__init__(name, left, right)
        self._name = name
        self._varname = varname

    @property
    def name(self):
        return self._name

    def reduce(self, tokens):
        return tokens
