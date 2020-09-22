import unittest

from src.core.core import create_person
from src.persist.db import db, get_data


class TestCreatePerson(unittest.TestCase):
    def test_create_person(self):

        """
        Should create new person in DB
        """

        # Act
        mydb = db("briw_test")
        create_person(mydb, "John", "Smith")
        result = get_data(mydb, "person")
        row = result[0]

        # Assert
        self.assertEqual(row[1], "John")
        self.assertEqual(row[2], "Smith")

        # Cleanup
        sql = f"DELETE FROM person WHERE id = {row[0]}"

        mycursor = mydb.cursor()
        mycursor.execute(sql)
        mydb.commit()
        mydb.close()


if __name__ == "__main__":
    unittest.main()