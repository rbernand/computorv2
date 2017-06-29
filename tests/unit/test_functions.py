import pytest

from computor import functions
from computor.parser import Parser
from computor.exceptions import ComputorError


def test_basics():
    parser = Parser()
    calc = parser.parse_calculation('1+1')
    functions.add('foo', calc)
    assert functions.get('foo') == calc
    with pytest.raises(ComputorError):
        functions.get('bar')
