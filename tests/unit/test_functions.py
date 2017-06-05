from computor import functions
from computor.parser import Parser


def test_basics():
    parser = Parser()
    calc = parser.parse_calculation('1+1')
    functions.add('foo', calc)
    assert functions.get('foo') == calc
