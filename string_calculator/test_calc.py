import pytest

from .calc import calculator


def test_calculator_with_empty_string_check_returns_zero():
    assert calculator('') == 0


def test_calculator_with_single_number_check_returns_number():
    assert calculator('53') == 53


def test_calculator_with_two_comma_separated_numbers_check_returns_sum():
    assert calculator('53,5') == 58


def test_calculator_with_newline_separated_numbers_check_returns_sum():
    assert calculator('53\n5') == 58


def test_calculator_with_three_comma_separated_numbers_check_returns_sum():
    assert calculator('53,5,11') == 69


def test_calculator_with_three_newline_separated_numbers_check_returns_sum():
    assert calculator('53\n5\n11') == 69


def test_calculator_with_three_numbers_one_comma_one_newline_check_returns_sum():
    assert calculator('53,5\n11') == 69


def test_calculator_with_negative_numbers_check_raises_error():
    with pytest.raises(Exception):
        calculator('-2')


def test_calculator_with_three_numbers_one_equals_1000_check_large_number_ignored():
    assert calculator('53,1000,5') == 1058


def test_calculator_with_three_numbers_one_gt_1000_check_large_number_ignored():
    assert calculator('53,5555,5') == 58
