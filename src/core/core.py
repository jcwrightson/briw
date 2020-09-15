import os
import csv

from src.constants import PEOPLE_FILE, DRINKS_FILE, PREFS_FILE
from src.models.models import Person, Drink, Preference
from src.persistence.files import read_rows


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


def create_person(name, age, the_dict):

    # Create a new `Person` using the class constructor method
    new_person = Person(len(the_dict), name, age)

    # Add this `Person` to our dictionary of `people`
    the_dict.update({new_person.id: new_person})

    return new_person


def create_drink(name, the_dict):

    # Create a new `Drink` using the class constructor method
    new_drink = Drink(len(the_dict), name)

    # Append this `Drink` to our dictionary of `drinks`
    the_dict.update({new_drink.id: new_drink})

    return new_drink


def create_pref(person: Person, drink: Drink, the_dict: dict):
    # A dictionary is a unique `key: value` data store
    # Let's use the id of our `Person` as the key, and the `Preference` object as the value

    new_pref = Preference(person, drink)

    # e.g: "2" : { person: { name: "John" }, drink: { name: "Beer" } }
    # new_dict_item = {person.id: new_pref}

    # Update dictionary
    the_dict.update({new_pref.person.id: new_pref})

    return new_pref


def get_prefs(people, drinks):

    data = {}

    rows = read_rows(PREFS_FILE)

    for row in rows:

        # each `row` looks like ['0','1']
        # row[0] is the id of the `Person` and row[1] is the id of the `Drink`

        # Swap `Person` id for a `Person` obj from our `people` dict
        person = people.get(row[0])

        # Do the same for `Drink`
        drink = drinks.get(row[1])

        # Create `Preference` from these two objects
        saved_pref = Preference(person, drink)

        # Update temp dict using `person.id` as our `key`
        data.update({person.id: saved_pref})

    return data


def get_people():

    # Create an empty list
    data = {}

    # get rows of data from our file
    rows = read_rows(PEOPLE_FILE)

    # Iterate over each row we get back from `read_rows`
    for row in rows:

        # Create a `Person` object using the `id`, and `name` stored in the row: ['123', 'Bob']
        saved_person = Person(row[0], row[1], int(row[2]))

        # add this to our temp dict
        data.update({saved_person.id: saved_person})

    # Return the dictionary of people back to the function caller
    return data


def get_drinks():

    data = {}

    rows = read_rows(DRINKS_FILE)

    for row in rows:

        saved_drink = Drink(row[0], row[1])

        data.update({saved_drink.id: saved_drink})

    return data
