from computor import LOG
from computor.exceptions import ComputorUnknownVariableError


VARIABLES = {}


def get(value):
    try:
        return VARIABLES[value]
    except KeyError:
        raise ComputorUnknownVariableError(value)


def add(key, value):
    if key in VARIABLES:
        LOG.warning("Overrinding variables '%s' = %f -> %f", key, VARIABLES[key], value)
    VARIABLES[key] = value
