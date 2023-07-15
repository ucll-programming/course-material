import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("string, expected_day, expected_month, expected_year", [
    (f'{day:02}/{month:02}/{year:04}', day, month, year)
    for day in [1, 5, 9, 10, 19, 28]
    for month in [1, 9, 12]
    for year in [0, 29, 994, 1980, 2022]
])
def test_parse_date(string, expected_day, expected_month, expected_year):
    actual_day = student.parse_day(string)
    actual_month = student.parse_month(string)
    actual_year = student.parse_year(string)

    assert expected_day == actual_day
    assert expected_month == actual_month
    assert expected_year == actual_year
