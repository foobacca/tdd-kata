import pytest

from .calc import calculator


def test_calculator_with_empty_string_check_returns_zero():
    assert calculator('') == 0


def test_calculator_with_single_number_check_returns_number():
    assert calculator('5') == 5


def test_calculator_with_two_numbers_with_comma_check_returns_sum():
    assert calculator('5,13') == 18


def test_calculator_with_two_numbers_with_newline_check_returns_sum():
    assert calculator('5\n13') == 18


def test_calculator_with_three_numbers_with_comma_newline_check_returns_sum():
    assert calculator('5,7\n13') == 25


def test_calculator_with_negative_number_check_error_raised():
    with pytest.raises(Exception):
        calculator('-3')


def test_calculator_with_number_gt_1000_check_ignored():
    assert calculator('5,1007\n13') == 18


def test_calculator_with_alternative_delimiter_check_delimiter_used():
    assert calculator('//#\n5#3#6') == 14
