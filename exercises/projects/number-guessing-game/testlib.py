import pytest


@pytest.fixture
def fake_input(monkeypatch):
    def func(inputs):
        def input(prompt=None):
            return str(next(iterator))

        iterator = iter(inputs)
        monkeypatch.setattr('builtins.input', input)

    return func


@pytest.fixture
def fake_random(monkeypatch):
    def func(values):
        def randint(a, b):
            assert a == 1
            assert b == 100
            return next(iterator)

        iterator = iter(values)
        monkeypatch.setattr('random.randint', randint)

    return func


@pytest.fixture
def read_stdout(capsys):
    def read():
        return capsys.readouterr().out.splitlines()
    return read
