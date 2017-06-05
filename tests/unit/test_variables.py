from computor import variables


def test_basics():
    variables.add('foo', 1)
    assert variables.get('foo') == 1
