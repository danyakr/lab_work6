from unittest import TestCase, main
from calculator.calculator import calculate


class CalculateTest(TestCase):

    def test_plus(self):
        self.assertEqual(calculate('1.2', '2.3', '+'), 3.5)

    def test_minus(self):
        self.assertEqual(calculate('1.3', '2.3', '-'), -1.0)

    def test_mult(self):
        self.assertEqual(calculate('1.3', '10', '*'), 13)

    def test_div(self):
        self.assertEqual(calculate('10', '3', '/'), 3.333333)

    def test_no_num(self):
        with self.assertRaises(ValueError) as e:
            calculate('a', 'b', '+')
        self.assertEqual(e.exception.args[0], 'Необходимо ввести числа!')

    def test_no_sign(self):
        with self.assertRaises(ValueError) as e:
            calculate('1', '2', 'a')
        self.assertEqual(e.exception.args[0], 'Необходимо выбрать операцию из списка!')

    def test_zero_divide(self):
        with self.assertRaises(ZeroDivisionError) as e:
            calculate('1', '0', '/')
        self.assertEqual(e.exception.args[0], 'Деление на ноль!')


if __name__ == '__main__':
    main()
