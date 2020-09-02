import os

from classes import Person, Drink, Preference, Round
from helpers import write_list, clear_screen, print_dict, print_list


def read_lines(file_name):
    try:
        the_file = open(file_name, "r")
        lines = the_file.readlines()
    except:
        return []
    return lines


def get_people():
    lines = read_lines("people.txt")
    data = []
    for line in lines:
        data.append(Person(line.strip()))
    return data


def get_drinks():
    lines = read_lines("drinks.txt")
    data = []
    for line in lines:
        data.append(Drink(line.strip()))
    return data


def save_people():
    write_list("people.txt", people, "name")


def save_drinks():
    write_list("drinks.txt", drinks, "name")


def save_and_exit():
    save_people()
    save_drinks()
    exit()


people = get_people()
drinks = get_drinks()
prefs = {}


def create_person(name):
    people.append(Person(name))


def create_drink(name):
    drinks.append(Drink(name))


menu = """
Please choose an option:

[1] List All People
[2] List All Drinks
[3] List All Preferences
[4] Create Person
[5] Create Drink
[6] Create Preference
[7] Exit

"""
exit_option = 7

while True:
    option = 0
    try:
        option = int(input(menu))
    except ValueError:
        print('Please enter a number')

    if option == 1:
        print_list(people, "People", "name")
    elif option == 2:
        print_list(drinks, "Drinks", "name")
    elif option == 3:
        print_dict(prefs, "Preferences", "name")
    elif option == 4:
        new_person = input("Please enter name: ")
        create_person(new_person)
        save_people()
    elif option == 5:
        new_drink = input("Please enter name: ")
        create_drink(new_drink)
        save_drinks()
    elif option == 6:

        selected_person = None
        selected_drink = None

        print_list(people, "People", "name")
        while selected_person == None:
            try:
                person_id = int(input("Please choose a person: "))
                selected_person = people[person_id]
            except:
                print("Invalid choice...")

        print_list(drinks, "Drinks", "name")

        while selected_drink == None:
            try:
                drink_id = int(input("Please choose a drink: "))
                selected_drink = drinks[drink_id]
            except:
                print("Invalid choice...")

        new_pref = Preference(selected_person, selected_drink)
        prefs.update({new_pref.person: new_pref.drink})

    elif option == exit_option:
        break

save_and_exit()
