import pytest
import student


def fake_input(inputs):
    def input():
        return str(next(iterator))
    iterator = iter(inputs)
    return input


@pytest.mark.parametrize("inputs", [
    [0],
    [1, 0],
    [1, 1, 0],
    [2, 1, 0],
    [1, 9, 2, 3, 8, 5, 4, 3, 2, 7, 0],
])
def test_sum_input(monkeypatch, capsys, inputs):
    monkeypatch.setattr('builtins.input', fake_input(inputs))

    student.sum_input()

    captured = capsys.readouterr()
    output = int(captured.out)
    expected = sum(inputs)

    assert expected == output
