import os

from src.constants import PEOPLE_FILE, DRINKS_FILE, PREFS_FILE
from src.models.models import Person, Drink, Preference, Round
from src.persistence.files import write_rows, write_prefs
from src.core.core import (
    clear_screen,
    print_table,
    create_drink,
    create_person,
    create_pref,
    get_drinks,
    get_people,
    get_prefs,
)

from src.persistence.db import db, get_data

# ============================================
# Define functions
# ============================================


def save_people(people: dict):
    write_rows(PEOPLE_FILE, people, ["id", "name", "age"])


def save_drinks(drinks: dict):
    write_rows(DRINKS_FILE, drinks, ["id", "name"])


def save_prefs(prefs: dict):
    write_prefs(PREFS_FILE, prefs)


def save_and_exit(people, drinks, prefs):

    try:
        save_people(people)
        save_drinks(drinks)
        save_prefs(prefs)
        print("Saved.")
    except Exception as e:
        print(f"Failed to save {e}")

    mydb.close()
    exit()


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

people = {}
drinks = {}
prefs = {}

# DB Handle
mydb = db()
result = get_data(mydb, "drink")
print(result)


# ============================================
# Start App
# ============================================


def refetch():

    global people
    global drinks
    global prefs

    people = get_people()
    drinks = get_drinks()
    prefs = get_prefs(people, drinks)


def main():

    # Clear Screen
    # clear_screen()

    # Fetch Data
    refetch()

    # Create infinite loop
    while True:

        # Init `option` variable
        option = None

        try:
            # Prompt user to choose an option
            option = int(input(menu))
        except ValueError:
            # If user entered a letter
            print("Please enter a number")

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
                    print("Pease try again")

            create_person(name, age, people)
            save_people(people)  # Update saved ppl file (optional)
            refetch()
        elif option == 5:
            # Prompt user to enter name
            name = input("Please enter name: ")
            create_drink(name, drinks)
            save_drinks(drinks)  # Update saved drinks file (optional)
            refetch()
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
            create_pref(selected_person, selected_drink, prefs)
            save_prefs(prefs)
            refetch()
    # Last thing we do before app terminates
    save_and_exit(people, drinks, prefs)


if __name__ == "__main__":

    main()
