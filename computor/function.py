from computor import LOG


FUNCTIONS = {}


def get(value):
    return FUNCTIONS[value]


def add(key, value):
    if key in FUNCTIONS:
        LOG.warning("Overrinding function '%s' = %f -> %f", key, FUNCTIONS[key], value)
    FUNCTIONS[key] = value
