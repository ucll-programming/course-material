import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("start, stop, step, expected", [
    (start, stop, step, list(range(start, stop, step)))
    for start, stop, step in [
        (0, 5, 1),
        (5, 10, 1),
        (10, 20, 1),
        (0, 5, 2),
        (10, 20, 2),
        (0, 5, 3),
        (5, 10, 3),
        (100, 200, 25),
        (10, 10, 1),
        (10, 1, 1),
    ]
])
def test_print_numbers(capsys, start, stop, step, expected):
    actual_return_value = student.print_numbers(start, stop, step)

    captured = capsys.readouterr()
    actual = [int(line) for line in captured.out.splitlines()]

    assert actual_return_value is None
    assert len(expected) == len(actual)
    for i in range(len(expected)):
        assert expected[i] == actual[i], f'Printed value #{i+1} should be {expected[i]} but was {actual[i]}'
