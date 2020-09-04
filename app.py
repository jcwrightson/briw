import os

from classes import Person, Drink, Preference, Round
from helpers import read_rows, clear_screen, print_table, write_rows, write_prefs

# ============================================
# Define functions
# ============================================


def get_people():

    # Create an empty list
    data = {}

    # get rows of data from our file
    rows = read_rows("people.csv")

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

    rows = read_rows("drinks.csv")

    for row in rows:

        saved_drink = Drink(row[0], row[1])

        data.update({saved_drink.id: saved_drink})

    return data


def get_prefs():

    data = {}

    rows = read_rows("prefs.csv")

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


def save_people():
    write_rows('people.csv', people, ["id", "name", "age"])


def save_drinks():
    write_rows('drinks.csv', drinks, ["id", "name"])


def save_prefs():
    write_prefs('prefs.csv', prefs)


def save_and_exit():

    try:
        save_people()
        save_drinks()
        save_prefs()
        print("Saved.")
    except Exception as e:
        print(f"Failed to save {e}")
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

    # Add this `Person` to our dictionary of `people`
    people.update({new_person.id: new_person})


def create_drink():

    # Prompt user to enter name
    name = input("Please enter name: ")

    # Create a new `Drink` using the class constructor method
    new_drink = Drink(len(drinks), name)

    # Append this `Drink` to our dictionary of `drinks`
    drinks.update({new_drink.id: new_drink})


def create_pref(person: Person, drink: Drink):
    # A dictionary is a unique `key: value` data store
    # Let's use the id of our `Person` as the key, and the `Preference` object as the value

    # e.g: "2" : { person: { name: "John" }, drink: { name: "Beer" } }
    new_dict_item = {person.id: Preference(person, drink)}

    # Update dictionary
    prefs.update(new_dict_item)


# ============================================
# Instantiate variables
# ============================================

version = 1.0

menu = f"""
Welcome to BrIW v{version}
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


# ============================================
# Start App
# ============================================

# Fetch data
people = get_people()
drinks = get_drinks()
prefs = get_prefs()

# Clear Screen
clear_screen()

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
        print_table(people, "people")  # Show list of ppl
    elif option == 2:
        print_table(drinks, "drinks")  # Show list of drinks
    elif option == 3:
        print_table(prefs, "prefs")  # Show list of prefs
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
        print_table(people, "people")

        # While they haven't selected a valid person
        while selected_person == None:
            try:
                # Prompt user to select a person's id
                person_id = input("Please choose a person: ")
                # Get that element from the person dict
                selected_person = people[person_id]
            except:
                # If user entered an id that doesn't exist
                print("Invalid choice...")

        # STEP #2
        # =========================================
        # Show user avail drinks in the drinks list
        print_table(drinks, "drinks")

        # While they haven't selected a valid drink
        while selected_drink == None:
            try:
                # Prompt user to select a drink's id
                drink_id = input("Please choose a drink: ")
                # Get that element from the drink dict
                selected_drink = drinks[drink_id]
            except:
                # If user entered an id that doesn't exist
                print("Invalid choice...")

        # STEP #3 and #4
        # ==========================================
        # Call create pref function to create a Preference and update dictionary
        create_pref(selected_person, selected_drink)


# Last thing we do before app terminates
save_and_exit()
