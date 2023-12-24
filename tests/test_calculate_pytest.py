import pytest
from calculator.calculator import calculate


def test_plus():
    assert calculate('1.2', '2.3', '+') == 3.5


def test_minus():
    assert calculate('1.3', '2.3', '-') == -1.0


def test_mult():
    assert calculate('1.3', '10', '*') == 13


def test_div():
    assert calculate('10', '3', '/') == 3.333333


def test_no_num():
    with pytest.raises(ValueError, match='Необходимо ввести числа!'):
        calculate('a', 'b', '+')


def test_no_sign():
    with pytest.raises(ValueError, match='Необходимо выбрать операцию из списка!'):
        calculate('1', '2', 'a')


def test_zero_divide():
    with pytest.raises(ZeroDivisionError, match='Деление на ноль!'):
        calculate('1', '0', '/')
