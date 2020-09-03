import os


def clear_screen():
    os.system("clear")


def print_list(some_list, title, prop):
    clear_screen()
    print(title.upper())
    print('-'*30)
    idx = 0
    for item in some_list:
        print(idx, "\t", item)
        idx += 1


def print_prefs(prefs):
    clear_screen()
    print("PREFERENCES")
    print('-'*30)
    for pref in prefs.values():
        print(pref)


def read_lines(file_name):
    try:
        the_file = open(file_name, "r")
        lines = the_file.readlines()
    except:
        return []
    return lines


def write_list(file_name, the_list, prop):
    try:
        the_file = open(file_name, "w")

        for item in the_list:
            the_file.write(getattr(item, prop) + "\n")
    finally:
        the_file.close()
