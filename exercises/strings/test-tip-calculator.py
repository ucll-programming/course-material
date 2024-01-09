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


@pytest.mark.timeout(1)
@pytest.mark.parametrize("cost, tip, expected", [
    ("100", "10", 110),
    ("100", "", 120),
    ("200", "", 240),
    ("200", "5", 210),
])
def test_tip_calculator(fake_input, capsys, cost, tip, expected):
    fake_input([cost, tip])

    student.tip_calculator()

    captured = capsys.readouterr()
    actual = captured.out
    assert f"You have to pay {expected}\n" == actual
