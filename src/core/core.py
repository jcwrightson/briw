import os
import csv

from src.models.models import Person, Drink, Preference
from src.persist.db import get_data, query, update


def clear_screen():
    os.system("clear")


def print_table(the_dict: dict, title: str):

    # Check if the dictionary is empty
    if len(the_dict) == 0:
        print("----empty----")

        # early return as to not execute the rest of the function for an empty dict
        return

    # Clear screen
    clear_screen()

    # Print the title as uppercase
    print(title.upper())

    # Print spacer line
    print("-" * 50)

    # Iterate through each object in the list
    for item in the_dict.values():

        # Indirectly call the `__str__` method on the object to get it's values as a string so we can print it: `id`, `name` etc...
        print(item)


def create_person(mydb, forename, surname):

    sql = "INSERT INTO person (forename, surname) values (%s, %s)"

    update(mydb, sql, (forename, surname))


def create_drink(mydb, name, description, price):

    sql = "INSERT INTO drink (name, description, price) values (%s, %s, %s)"

    update(mydb, sql, (name, description, price))


def create_pref(mydb, person, drink):

    sql = "UPDATE person SET drink = %s WHERE id = %s"

    update(mydb, sql, (drink.id, person.id))


def get_prefs(mydb):

    data = {}

    sql = "SELECT * FROM person p JOIN drink d ON p.drink = d.id"

    rows = query(mydb, sql)

    for row in rows:

        person = Person(row[0], row[1], row[2], row[3])
        drink = Drink(row[4], row[5], row[6], row[7])

        # Create `Preference` from these two objects
        saved_pref = Preference(person, drink)

        # Update temp dict using `person.id` as our `key`
        data.update({person.id: saved_pref})

    return data


def get_people(mydb):

    # Create an empty list
    data = {}

    # get rows of data from our file
    rows = get_data(mydb, "person")

    # Iterate over each row we get back from `read_rows`
    for row in rows:

        # Create a `Person` object using the `id`, and `name` stored in the row: ['123', 'Bob']
        saved_person = Person(row[0], row[1], row[2], row[3])

        # add this to our temp dict
        data.update({saved_person.id: saved_person})

    # Return the dictionary of people back to the function caller
    return data


def get_drinks(mydb):

    data = {}

    rows = get_data(mydb, "drink")

    for row in rows:

        saved_drink = Drink(row[0], row[1], row[2], row[3])

        data.update({saved_drink.id: saved_drink})

    return data
