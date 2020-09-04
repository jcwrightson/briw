import os
import csv


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
    print('-'*50)

    # Iterate through each object in the list
    for item in the_dict.values():

        # Indirectly call the `__str__` method on the object to get it's values as a string so we can print it: `id`, `name` etc...
        print(item)


def read_rows(filename: str):

    # Create empty list
    rows = []

    try:
        # try to open `.csv` file
        with open(filename) as csvfile:

            # Create a new `reader` using the `csv` module and give it our file to read
            reader = csv.reader(csvfile)

            # Iterate and read each row
            for row in reader:

                # Append each row read to our temp list
                rows.append(row)

    except FileNotFoundError:
        print(f"Failed to load {filename}")

    # Return a list of rows back to caller
    return rows


def write_rows(file_name: str, rows: dict, fields: list):

    def build_row(row):
        r = []
        for field in fields:
            r.append(getattr(row, field))
        return r

    with open(file_name, 'w', newline='\n') as csvfile:

        writer = csv.writer(csvfile)

        for row in rows.values():

            writer.writerow(build_row(row))


def write_prefs(file_name: str, prefs: dict):

    with open(file_name, 'w', newline='\n') as csvfile:

        writer = csv.writer(csvfile)

        for pref in prefs.values():

            writer.writerow([pref.person.id, pref.drink.id])
