import unittest
from unittest.mock import patch
from calculator.cont_mgr_calc import BatchCalculatorContextManager


class TestBatchCalculatorContextManager(unittest.TestCase):

    def test_file_is_closed(self):
        with patch('builtins.open') as mock_open:
            mock_file = mock_open.return_value
            context_manager = BatchCalculatorContextManager('test_file.txt')
            with context_manager as f:
                pass  # Не требуется действий с файлом

            mock_file.close.assert_called_once()

    def test_file_is_opened(self):
        with patch('builtins.open') as mock_open:
            context_manager = BatchCalculatorContextManager('test_file.txt')
            with context_manager as f:
                pass  # Не требуется действий с файлом

            mock_open.assert_called_once_with('test_file.txt')


if __name__ == '__main__':
    unittest.main()
