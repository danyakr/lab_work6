from unittest import TestCase, main
from unittest.mock import patch
import sys
import io
from calculator.calculator import convert_precision


class ConvertPrecisionTest(TestCase):

    def test_normal_precision(self):
        with patch('sys.stdout', new_callable=io.StringIO):
            self.assertEqual(convert_precision('0.001'), 3)
            self.assertEqual(convert_precision('1e-6'), 6)

    def test_int_precision(self):
        with patch('sys.stdout', new_callable=io.StringIO):
            self.assertEqual(convert_precision('10'), 6)
            self.assertEqual(convert_precision('1'), 6)
            self.assertEqual(convert_precision('0'), 0)

    def test_negative_precision(self):
        with patch('sys.stdout', new_callable=io.StringIO):
            self.assertEqual(convert_precision('-10'), 6)
            self.assertEqual(convert_precision('-1'), 6)

    def test_no_precision(self):
        with patch('sys.stdout', new_callable=io.StringIO):
            self.assertEqual(convert_precision('abcd'), 6)
            self.assertEqual(convert_precision('1e+3'), 6)
            self.assertEqual(convert_precision('1e'), 6)
            self.assertEqual(convert_precision(''), 6)


if __name__ == '__main__':
    main()
