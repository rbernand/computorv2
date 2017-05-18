from computor.variables import Variables


def test_basics():
    Variables.add('foo', 1)
    assert Variables.get('foo') == 1
