from computor import LOG
from computor.tokens import Token
from computor.exceptions import ComputorUnknownFunctionError


FUNCTIONS = {}


def get(value):
    try:
        return FUNCTIONS[value]
    except KeyError:
        raise ComputorUnknownFunctionError(value)


def add(key, value):
#    if not isinstance(value, Token):
#        raise ComputorTypeError(value, Token)
    if key in FUNCTIONS:
        # TODO: temporary, edit lexer/parser then this
        LOG.warning("Overrinding function '%s' = %s -> %s",
                    key,
                    FUNCTIONS[key].tostring(),
                    value.tostring())
    FUNCTIONS[key] = value
