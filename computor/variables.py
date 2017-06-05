from computor import LOG


VARIABLES = {}


def get(value):
    return VARIABLES[value]


def add(key, value):
    if key in VARIABLES:
        LOG.warning("Overrinding variables '%s' = %f -> %f", key, VARIABLES[key], value)
    VARIABLES[key] = value
