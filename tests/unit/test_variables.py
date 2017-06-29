import pytest

from computor import variables
from computor.exceptions import ComputorError


def test_basics():
    variables.add('foo', 1)
    assert variables.get('foo') == 1
    with pytest.raises(ComputorError):
        variables.get('bar')
