import os

from classes import Person, Drink, Preference, Round
from helpers import read_rows, read_lines, write_list, clear_screen, print_list, write_rows

# ============================================
# Define functions
# ============================================


def get_people():

    # Create an empty list
    data = []

    # get rows of data from our file
    rows = read_rows("people.csv")

    # Iterate over each row we get back from `read_rows`
    for row in rows:

        # Create a `Person` object using the `id`, and `name` stored in the row: ['123', 'Bob']
        saved_person = Person(int(row[0]), row[1], int(row[2]))

        # add this to our temp list
        data.append(saved_person)

    # Return the list of people back to the function caller
    return data


def get_drinks():

    data = []

    rows = read_rows("drinks.csv")

    for row in rows:

        saved_drink = Drink(int(row[0]), row[1])

        data.append(saved_drink)

    return data


def save_people():
    write_rows('people.csv', people, ["id", "name", "age"])


def save_drinks():
    write_rows('drinks.csv', drinks, ["id", "name"])


def save_and_exit():
    save_people()
    save_drinks()
    exit()


def create_person():

    # Prompt user to enter name
    name = input("Please enter name: ")

    # Create `age` variable
    age = None

    # While user hasn't entered a valid age
    while age == None:
        try:
            # Prompt user to enter age
            age = int(input("Please enter age: "))
        except:
            print('Pease try again')

    # Create a new `Person` using the class constructor method
    new_person = Person(len(people), name, age)

    # Append this `Person` to the end of our list of `people`
    people.append(new_person)


def create_drink():

    # Prompt user to enter name
    name = input("Please enter name: ")

    # Create a new `Drink` using the class constructor method
    new_drink = Drink(len(drinks), name)

    # Append this `Drink` to the end our list of `drinks`
    drinks.append(new_drink)


def create_pref(person: Person, drink: Drink):
    # A dictionary is a unique `key: value` data store
    # Let's use the name of our `Person` as the key, and the `Preference` object as the value

    # e.g: "John" : { person: { name: "John" }, drink: { name: "Beer" } }
    new_dict_item = {person.name: Preference(person, drink)}

    # Update dictionary
    prefs.update(new_dict_item)


# ============================================
# Instantiate variables
# ============================================

menu = """
Please choose an option:

[1] List All People
[2] List All Drinks
[3] List All Preferences
[4] Create Person
[5] Create Drink
[6] Create Preference
[0] Exit

"""
exit_option = 0
people = get_people()
drinks = get_drinks()
prefs = {}


# ============================================
# Start App
# ============================================


# Create infinite loop
while True:

    # Init `option` variable
    option = None

    try:
        # Prompt user to choose an option
        option = int(input(menu))
    except ValueError:
        # If user entered a letter
        print('Please enter a number')

    # If user entered a valid option we make it here
    if option == exit_option:
        # Break out the loop if user selects `exit_option`
        break
    elif option == 1:
        print_list(people, "people")  # Show list of ppl
    elif option == 2:
        print_list(drinks, "drinks")  # Show list of drinks
    elif option == 3:
        print_list(prefs, "prefs", True)  # Show list of prefs
    elif option == 4:
        create_person()
        save_people()  # Update saved ppl file (optional)
    elif option == 5:
        create_drink()
        save_drinks()  # Update saved drinks file (optional)
    elif option == 6:

        # Create Preference Object: { person: Person, drink: Drink }
        # =============================================================
        #
        # 1. User needs to select a person. (Person)
        # 2. User needs to select a drink. (Drink)
        # 3. We need to put the two together. (Preference)
        # 4. We need to update the local (in memory) dictionary (prefs)

        # Init some variables to None
        selected_person = None
        selected_drink = None

        # STEP #1
        # =========================================
        # Show user avail ppl in the people list
        print_list(people, "people")

        # While they haven't selected a valid person
        while selected_person == None:
            try:
                # Prompt user to select a person's idx
                person_idx = int(input("Please choose a person: "))
                # Get that element from the person list
                selected_person = people[person_idx]
            except:
                # If user entered a letter, or chose an idx that doesn't exist
                print("Invalid choice...")

        # STEP #2
        # =========================================
        # Show user avail drinks in the drinks list
        print_list(drinks, "drinks")

        # While they haven't selected a valid drink
        while selected_drink == None:
            try:
                # Prompt user to select a drink's idx
                drink_idx = int(input("Please choose a drink: "))
                # Get that element from the drink list
                selected_drink = drinks[drink_idx]
            except:
                # If user entered a letter, or chose an idx that doesn't exist
                print("Invalid choice...")

        # STEP #3 and #4
        # ==========================================
        # Call create pref function to create a Preference and update dictionary
        create_pref(selected_person, selected_drink)


# Last thing we do before app terminates
save_and_exit()
