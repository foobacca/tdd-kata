import pytest

from .calc import calc, StringCalculator


def test_calc_with_empty_string_check_returns_zero():
    assert calc('') == 0


def test_calc_with_number_string_check_returns_number():
    assert calc('4') == 4


def test_calc_with_number_comma_number_returns_sum():
    assert calc('4,23') == 27


def test_calc_with_number_newline_number_returns_sum():
    assert calc('4\n23') == 27


def test_calc_with_number_comma_number_newline_number_returns_sum():
    assert calc('13,4\n23') == 40


def test_calc_with_negative_number_raises_error():
    with pytest.raises(Exception):
        calc('-3')


def test_calc_with_number_gt_1000_check_number_ignored():
    assert calc('13,4\n1023') == 17


def test_calc_with_custom_single_char_delim_check_delim_used():
    assert calc('//#\n13#4') == 17


def test_calc_with_custom_single_char_delim_check_comment_chars_not_used():
    with pytest.raises(Exception):
        calc('//#\n13/4')


def test_calc_with_custom_multi_char_delim_check_delim_used():
    assert calc('//[###]\n13###4') == 17


def test_calc_with_custom_multi_char_delim_check_subdelimeter_raises_error():
    with pytest.raises(Exception):
        calc('//[###]\n13#4')


def test_calc_with_custom_multi_and_single_char_delim_check_delim_used():
    assert calc('//[###][,]\n13,4###23') == 40


def test_stringcalculator_with_multi_and_single_char_delim_check_delimiters():
    sc = StringCalculator('//[###][,]\n13,4###23')
    assert sc.delimeters == ['###', ',']
