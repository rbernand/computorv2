import pytest
import mock

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


def test_run(monkeypatch):
    mock_exe_assignation = mock.MagicMock()
    mock_exe_calculation = mock.MagicMock()
    mock_exe_command = mock.MagicMock()
    monkeypatch.setattr(Executor, 'execute_assignation', mock_exe_assignation)
    monkeypatch.setattr(Executor, 'execute_calculation', mock_exe_calculation)
    monkeypatch.setattr(Executor, 'execute_command', mock_exe_command)

    executor = Executor('1+1'); executor.run();
    assert mock_exe_calculation.call_count == 1

    executor = Executor('1+1=?'); executor.run()
    assert mock_exe_calculation.call_count == 2

    executor = Executor('a=2'); executor.run()
    assert mock_exe_assignation.call_count == 1

    executor = Executor('fun(x)=x+1'); executor.run()
    assert mock_exe_assignation.call_count == 2
