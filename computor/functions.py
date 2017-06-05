from computor import LOG
from computor.tokens import Token
# from computor.exceptions import ComputorTypeError


FUNCTIONS = {}


def get(value):
    return FUNCTIONS[value]


def add(key, value):
#    if not isinstance(value, Token):
#        raise ComputorTypeError(value, Token)
    if key in FUNCTIONS:
    	# TODO: temporary, edit lexer/parser then this
        LOG.warning("Overrinding function '%s' = %f -> %f", key, FUNCTIONS[key], Token("1"))
    FUNCTIONS[key] = value
