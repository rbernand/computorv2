from computor import variables
from computor.tokens import Variable


def test_basics():
    variables.add('foo', 1)
    assert variables.get('foo') == 1
