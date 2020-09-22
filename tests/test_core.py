import unittest
from unittest.mock import patch, Mock

from src.core.core import print_table


class TestCore(unittest.TestCase):
    @patch("builtins.print")
    def test_print_table_empty(self, mock_print):

        print_table({}, "Test")

        mock_print.assert_called_once()
        mock_print.assert_called_with("----empty----")

    @patch("builtins.print")
    def test_print_table(self, mock_print):

        print_table({"id": 1}, "Test")

        self.assertEqual(mock_print.call_count, 3)


if __name__ == "__main__":
    unittest.main()