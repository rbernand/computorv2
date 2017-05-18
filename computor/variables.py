from computor import log


class Variables:
    VARIABLES = {}

    def __init__(self, *args, **kwargs):
        raise NotImplementedError('Container class')

    @classmethod
    def get(cls, value):
        return cls.VARIABLES[value]

    @classmethod
    def add(self, key, value):
        if key in Variables.VARIABLES:
            log.warning("Overrinding variables '%s' = %f -> %f",
                        key, Variables.VARIABLES[key], value)
        Variables.VARIABLES[key] = value
