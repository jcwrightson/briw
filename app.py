import os

from classes import Person, Drink, Preference, Round


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


# def save_and_exit():
#     write_data("people.txt", people)
#     write_data("drinks.txt", drinks)
#     write_data("prefs.txt", prefs)


people = get_people()
drinks = get_drinks()
prefs = {}


def cls():
    os.system("clear")


def print_dict(some_dict, title, prop):
    cls()
    print(title.upper())
    print('-'*30)
    for key, val in some_dict.items():
        print(getattr(key, prop), "\t"+getattr(val, prop))


def print_list(some_list, title, prop):
    cls()
    print(title.upper())
    print('-'*30)
    idx = 0
    for item in some_list:
        print(idx, "\t" + getattr(item, prop))
        idx += 1


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


cls()
while True:
    option = 0
    try:
        option = int(input(menu))
    except ValueError:
        print('Plese enter a number')

    if option == 1:
        print_list(people, "People", "name")
    elif option == 2:
        print_list(drinks, "Drinks", "name")
    elif option == 3:
        print_dict(prefs, "Preferences", "name")
    elif option == 4:
        new_person = input("Please enter name: ")
        create_person(new_person)
    elif option == 5:
        new_drink = input("Please enter name: ")
        create_drink(new_drink)
    elif option == 6:

        selected_person = None
        selected_drink = None

        print_list(people, "People", "name")
        while selected_person == None:
            try:
                person_id = int(input("Please choose a person: "))
                selected_person = people[person_id]
            except:
                pass

        print_list(drinks, "Drinks", "name")

        while selected_drink == None:
            try:
                drink_id = int(input("Please choose a drink: "))
                selected_drink = drinks[drink_id]
            except:
                pass

        new_pref = Preference(selected_person, selected_drink)
        prefs.update({new_pref.person: new_pref.drink})

    elif option == exit_option:
        break

# save_and_exit()
