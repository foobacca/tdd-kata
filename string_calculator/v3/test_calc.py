import pytest

from .calc import calculator


def test_calculator_with_empty_string_check_returns_zero():
    assert calculator('') == 0


def test_calculator_with_single_number_check_returns_number():
    assert calculator('3') == 3


def test_calculator_with_number_comma_number_check_returns_sum():
    assert calculator('3,5') == 8


def test_calculator_with_number_newline_number_check_returns_sum():
    assert calculator('3\n5') == 8


def test_calculator_with_number_comma_number_newline_number_check_returns_sum():
    assert calculator('15,3\n5') == 23


def test_calculator_with_negative_number_check_raises_error():
    with pytest.raises(Exception):
        calculator('-30')


def test_calculator_with_number_over_1000_check_number_ignored():
    assert calculator('15,1003\n5') == 20


def test_calculator_with_custom_single_char_delimiter_check_returns_sum():
    assert calculator('//#\n15#5') == 20


def test_calculator_with_custom_multi_char_delimiter_check_returns_sum():
    assert calculator('//[###]\n15###5') == 20


def test_calculator_with_multi_char_delimiter_spec_bad_delim_used_check_raise_error():
    with pytest.raises(Exception):
        calculator('//[###]\n15##5')


def test_calculator_with_custom_multi_char_delimiter_2_check_returns_sum():
    assert calculator('//[#,#]\n15#,#5') == 20
