class ComputorError(Exception):
    pass


class ComputorSyntaxError(ComputorError, SyntaxError):
    pass


class ComputorTypeError(ComputorError, TypeError):
    def __init__(self, value, *expected):
        super().__init__()
        self.value = value
        self.expected = expected

    def __str__(self):
        out = "Invalid type '%s'" % self.value.__name__
        if self.expected:
            out += '\nExpected: ' + ', '.join(x.__name__ for x in self.expected)
        return out


class ComputorUnknownCommandError(ComputorError):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return "Unknown command: '%s'" % self.msg


class ComputorUnknownVariableError(ComputorError):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return "Unknown variable: '%s'" % self.msg


class ComputorUnknownFunctionError(ComputorError):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return "Unknown function: '%s'" % self.msg
