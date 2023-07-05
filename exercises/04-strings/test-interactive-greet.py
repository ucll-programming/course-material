import pytest
import student


@pytest.fixture
def fake_input(monkeypatch):
    def func(inputs):
        def input(prompt=None):
            return str(next(iterator))

        iterator = iter(inputs)
        monkeypatch.setattr('builtins.input', input)

    return func


@pytest.mark.parametrize("name, expected", [
    ("John", "Hello, John!\n"),
    ("Fionnula", "Hello, Fionnula!\n"),
    ("Saoirse", "Hello, Saoirse!\n"),
])
def test_interactive_greet(fake_input, capsys, name, expected):
    fake_input([name])

    student.interactive_greet()

    captured = capsys.readouterr()
    actual = captured.out
    assert expected == actual
