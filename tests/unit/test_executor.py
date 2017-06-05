import pytest

from computor.executor import Executor


def test_basics():
    executor = Executor("1+1")
    assert executor.is_calculation()
    assert executor.type == Executor.Type.CALCULATION
    executor = Executor("1+1")
    assert executor.is_calculation()
    assert executor.type == Executor.Type.CALCULATION
    executor = Executor("1+1=?")
    assert executor.is_calculation()
    assert executor.type == Executor.Type.CALCULATION
    executor = Executor("a=1+1")
    assert executor.is_assignation()
    assert executor.type == Executor.Type.ASSIGNATION
    executor = Executor("fun(x)=1+1")
    assert executor.is_assignation()
    assert executor.type == Executor.Type.ASSIGNATION


def test_i_is_not_a_valid_name():
    with pytest.raises(SyntaxError):
        Executor("1=1=1")
    with pytest.raises(SyntaxError):
        Executor("i=2")
    with pytest.raises(SyntaxError):
        Executor("i(x)=11")
    with pytest.raises(SyntaxError):
        Executor("fun(i)=1")
    with pytest.raises(SyntaxError):
        Executor("i(i)=1")
