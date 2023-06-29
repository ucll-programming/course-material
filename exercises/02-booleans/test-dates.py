from datetime import datetime
import pytest
import calendar
import student


def does_function_exist(function_name):
    return function_name in dir(student)


def if_function_exists(function_name):
    return pytest.mark.skipif(not does_function_exist(function_name), reason=f'{function_name} not found in student module')


@pytest.mark.parametrize('function_name', [
    'is_leap_year',
    'has_30_days',
    'has_31_days',
    'has_28_days',
    'has_29_days',
    'is_valid_month',
    'is_valid_date',
])
def test_check_function_existence(function_name):
    assert function_name in dir(student), f'{function_name} not defined'


@if_function_exists('is_leap_year')
@pytest.mark.parametrize('year', range(1000, 2400, 5))
def test_is_leap_year(year):
    actual = student.is_leap_year(year=year)
    expected = calendar.isleap(year)

    assert expected == actual, f'is_leap_year({year}) should return {expected}'


@if_function_exists('has_30_days')
@pytest.mark.parametrize('month', range(1, 13))
def test_has_30_days(month):
    actual = student.has_30_days(month=month)
    expected = calendar.monthrange(2000, month)[1] == 30

    assert expected == actual, f'has_30_days({month}) should return {expected}'


@if_function_exists('has_31_days')
@pytest.mark.parametrize('month', range(1, 13))
def test_has_31_days(month):
    actual = student.has_31_days(month=month)
    expected = calendar.monthrange(2000, month)[1] == 31
    assert expected == actual, f'has_31_days({month}) should return {expected}'


@if_function_exists('has_28_days')
@pytest.mark.parametrize('month', range(1, 13))
@pytest.mark.parametrize('year', [1900, 1904, 2000, 2400, 2012, 2013, 2014, 2015])
def test_has_28_days(month, year):
    actual = student.has_28_days(month=month, year=year)
    expected = calendar.monthrange(year, month)[1] == 28

    assert expected == actual, f'has_28_days({month}, {year}) should return {expected}'


@if_function_exists('has_29_days')
@pytest.mark.parametrize('month', range(1, 13))
@pytest.mark.parametrize('year', [1900, 1904, 2000, 2400, 2012, 2013, 2014, 2015])
def test_has_29_days(month, year):
    actual = student.has_29_days(month=month, year=year)
    expected = calendar.monthrange(year, month)[1] == 29

    assert expected == actual, f'has_29_days({month}, {year}) should return {expected}'


@if_function_exists('is_valid_month')
@pytest.mark.parametrize('month', range(1, 13))
def test_is_valid_month(month):
    actual = student.is_valid_month(month=month)
    assert actual == True, f'is_valid_month({month}) should return True'


@if_function_exists('is_valid_month')
@pytest.mark.parametrize('month', [-5, 0, 13, 19])
def test_is_not_valid_month(month):
    actual = student.is_valid_month(month=month)
    assert actual == False, f'is_valid_month({month}) should return False'


@if_function_exists('is_valid_date')
@pytest.mark.parametrize('day', [1, 4, 15, 28, 29, 30, 31, 32])
@pytest.mark.parametrize('month', range(1, 13))
@pytest.mark.parametrize('year', [1900, 1904, 2000, 2400, 2012, 2013, 2014, 2015])
def test_is_valid_date(day, month, year):
    actual = student.is_valid_date(day=day, month=month, year=year)
    try:
        datetime(year=year, month=month, day=day)
        expected = True
    except:
        expected = False

    assert expected == actual, f'is_valid_date({day}, {month}, {year}) should return {expected}'
