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
@pytest.mark.parametrize("inputs", [
    [0],
    [1, 0],
    [1, 1, 0],
    [2, 1, 0],
    [1, 9, 2, 3, 8, 5, 4, 3, 2, 7, 0],
])
def test_sum_input(capsys, fake_input, inputs):
    fake_input(inputs)

    actual_return_value = student.sum_input()

    captured = capsys.readouterr()
    output = captured.out
    expected = f'The sum equals {sum(inputs)}\n'

    assert expected == output
    assert actual_return_value is None
