import os


def read_data(file_name):
    idx = 0
    data = {}
    try:
        the_file = open(file_name, "r")
        lines = the_file.readlines()

        for line in lines:
            data.update({idx: line.strip()})
            idx += 1

        the_file.close()

    except FileNotFoundError:
        print(f"{file_name} not found")

    return data


def write_data(file_name, data):
    try:
        the_file = open(file_name, "w")

        for line in data.values():
            the_file.write(line + "\n")
    finally:
        the_file.close()


def save_and_exit():
    write_data("people.txt", people)
    write_data("drinks.txt", drinks)


# id:name
people = read_data("people.txt")

# id:name
drinks = read_data("drinks.txt")

# person:drink
favs = {}


def cls():
    os.system("clear")


def print_table(some_dict, title):
    cls()
    print(title.upper())
    print('-'*30)
    for key, val in some_dict.items():
        print(key, val)
        print()


def create_person(name):
    people.update({len(people): name})


menu = """
Please choose an option:

[1] List All People
[2] List All Drinks
[3] List All Favourites
[4] Create Person
[5] Select Person's Favourite
[6] Exit

"""
exit_option = 6


cls()
while True:
    option = 0
    try:
        option = int(input(menu))
    except ValueError:
        print('Plese enter a number')

    if option == 1:
        print_table(people, 'People')
    elif option == 2:
        print_table(drinks, 'Drinks')
    elif option == 3:
        print_table(favs, 'Favourites')
    elif option == 4:
        new_person = input("Please enter name: ")
        create_person(new_person)
    elif option == 5:

        person_id = None
        drink_id = None

        print_table(people, 'People')
        while person_id not in people.keys():
            try:
                person_id = int(input("Please choose a person: "))
            except ValueError:
                print('Please enter a number')

        print_table(drinks, 'Drinks')
        while drink_id not in drinks.keys():
            try:
                drink_id = int(input("Please choose a drink: "))
            except ValueError:
                print('Please enter a number')

        person_val = people.get(person_id)
        drink_val = drinks.get(drink_id)
        favs.update({person_val: drink_val})

    elif option == exit_option:
        break

save_and_exit()
