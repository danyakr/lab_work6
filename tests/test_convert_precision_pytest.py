import pytest
from calculator.calculator import convert_precision


def test_normal_precision():
    assert convert_precision('0.001') == 3
    assert convert_precision('1e-6') == 6


def test_int_precision():
    assert convert_precision('10') == 6
    assert convert_precision('1') == 6
    assert convert_precision('0') == 0


def test_negative_precision():
    assert convert_precision('-10') == 6
    assert convert_precision('-1') == 6


def test_no_precision():
    assert convert_precision('abcd') == 6
    assert convert_precision('1e+3') == 6
    assert convert_precision('1e') == 6
    assert convert_precision('') == 6
