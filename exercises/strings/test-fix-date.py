import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("date, expected", [
    (
        f'{month:02}/{day:02}/{year:04}',
        f'{year:04}/{month:02}/{day:02}',
    )
    for day in [1, 9, 15, 28]
    for month in [1, 8, 12]
    for year in [0, 9, 28, 391, 1800]
])
def test_fix_date(date, expected):
    actual = student.fix_date(date)
    assert expected == actual, f'fix_date({date!r}) should be equal to {expected!r} but got {actual!r}'
