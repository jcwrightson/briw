import unittest
from unittest.mock import patch, Mock
from src.core.core import print_list, print_countries


from src.models.drink import Drink


class Test_Core(unittest.TestCase):

    @patch("builtins.print")
    def test_print_list(self, mock_print):

        the_list = ["John", "Paul", "Ringo", "George"]

        print_list(the_list)

        self.assertEqual(mock_print.call_count, 4)

    @patch("core.get_countries", return_value=["Spain", "Germany"])
    def test_print_countries(self, mock_get_countries):

        print_countries()
        mock_get_countries.assert_called_once()
        # self.assertEqual(mock_print.call_count, 2)

        Mock(Drink)


if __name__ == "__main__":
    unittest.main()
