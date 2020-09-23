import unittest
from unittest.mock import patch, Mock

from src.core.core import print_table
from src.persist.db import get_data, update_with_dict


class TestGetData(unittest.TestCase):
    def test_get_data(self):
        """Executes correct sql query"""

        mock_db = Mock()

        get_data(mock_db, "test")

        mock_db.cursor().execute.assert_called_with("SELECT * FROM test LIMIT 100")
        mock_db.cursor().fetchall.assert_called_once()

    @patch("src.persist.db.update")
    def test_update_with_dict(self, mock_update):

        test_data = {"a": 1, "b": 2, "c": 3}
        mock_db = Mock()
        update_with_dict(mock_db, "test", test_data)

        expectedSQL = "INSERT INTO test (a, b, c) VALUES(%s, %s, %s)"

        self.assertEqual(mock_update.call_args.args[0], expectedSQL)



if __name__ == "__main__":
    unittest.main()