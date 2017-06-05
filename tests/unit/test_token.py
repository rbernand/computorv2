from computor.parser import Token

def test_parsing():
    a = Token(1,
              Token(2, None, None),
              Token(3, None, None))
    assert a == a
    assert a == Token(1,
                      Token(2, None, None),
                      Token(3, None, None))
    assert a != Token(10,
                      Token(2, None, None),
                      Token(3, None, None))
    assert a != Token(1,
                      Token(20, None, None),
                      Token(3, None, None))
    assert a != Token(10,
                      None,
                      Token(3, None, None))
