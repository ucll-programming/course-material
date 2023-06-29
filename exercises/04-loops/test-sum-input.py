import pytest
import student


@pytest.fixture
def fake_inputs(monkeypatch):
    def func(inputs):
        def input():
            return str(next(iterator))

        iterator = iter(inputs)
        monkeypatch.setattr('builtins.input', input)

    return func


@pytest.mark.parametrize("inputs", [
    [0],
    [1, 0],
    [1, 1, 0],
    [2, 1, 0],
    [1, 9, 2, 3, 8, 5, 4, 3, 2, 7, 0],
])
def test_sum_input(capsys, fake_inputs, inputs):
    fake_inputs(inputs)

    student.sum_input()

    captured = capsys.readouterr()
    output = int(captured.out)
    expected = sum(inputs)

    assert expected == output
