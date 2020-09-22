import unittest
from unittest.mock import patch, Mock

from src.core.core import print_table
from src.persist.db import get_data


class TestGetData(unittest.TestCase):
    def test_get_data(self):
        """Executes correct sql query"""

        mock_db = Mock()

        get_data(mock_db, "test")

        mock_db.cursor().execute.assert_called_with("SELECT * FROM test LIMIT 100")
        mock_db.cursor().fetchall.assert_called_once()


if __name__ == "__main__":
    unittest.main()