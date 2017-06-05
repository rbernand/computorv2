class ComputorError(Exception):
    pass


class ComputorSyntaxError(ComputorError, SyntaxError):
    pass


class ComputorTypeError(ComputorError, TypeError):
    pass


class ComputorUnknownCommandError(ComputorError):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return "Unknown command: '%s'" % self.msg
