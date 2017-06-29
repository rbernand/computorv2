import mock

import prompt_toolkit


def test_prompt_command(monkeypatch):
    expected = [
        "foo bar",
        "something else is other thing "
    ]
    monkeypatch.setattr(prompt_toolkit, 'prompt', mock.MagicMock(side_effect=expected))
    from computor.__main__ import prompt_command
    for expect, receive in zip(expected, prompt_command()):
        assert expect == receive


def test_clear_line():
    from computor.__main__ import _clear_line

    lines = [
        ("abc", "abc"),
        ("abc def", "abcdef"),
        ("abc              def", "abcdef"),
        ("          abc def              ", "abcdef")
    ]
    for (line, expected) in lines:
        assert _clear_line(line) == expected


def test_main_loop(monkeypatch):
    exe = mock.MagicMock()
    from computor.__main__ import main_loop
    monkeypatch.setattr('computor.__main__.Executor', exe)

    def dada():
        def foo():
            yield 'foo'
            yield 'bar'
            yield '1+1'
        return foo()

    main_loop(dada)
    exe.assert_any_call('foo')
    exe.assert_any_call('bar')
    exe.assert_any_call('1+1')
