import unittest

from src.core.core import create_drink
from src.persist.db import db, get_data


class TestCreateDrink(unittest.TestCase):
    def test_create_drink(self):

        """
        Should create new drink in DB
        """

        # Act
        mydb = db("briw_test")
        create_drink(mydb, "Beer", None, 2)
        result = get_data(mydb, "drink")
        row = result[0]

        # Assert
        self.assertEqual(row[1], "Beer")
        self.assertEqual(row[2], None)
        self.assertEqual(row[3], 2)

        # Cleanup
        sql = f"DELETE FROM drink WHERE id = {row[0]}"

        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        mydb.close()


if __name__ == "__main__":
    unittest.main()