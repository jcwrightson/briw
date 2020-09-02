import os

def clear_screen():
    os.system("clear")


def print_dict(some_dict, title, prop):
    clear_screen()
    print(title.upper())
    print('-'*30)
    for key, val in some_dict.items():
        print(getattr(key, prop), "\t"+getattr(val, prop))


def print_list(some_list, title, prop):
    clear_screen()
    print(title.upper())
    print('-'*30)
    idx = 0
    for item in some_list:
        print(idx, "\t" + getattr(item, prop))
        idx += 1


def read_data(file_name):

    data = {}

    try:
        the_file = open(file_name, "r")
        lines = the_file.readlines()

        for line in lines: # '0, Beer'

            [key, val] = line.split(', ')  # ['0','Beer']
            try:
                data.update({int(key): val.strip()})
            except:
                data.update({key: val.strip()})

        the_file.close()

    except FileNotFoundError:
        print(f"{file_name} not found")

    return data


def write_data(file_name, data):
    try:
        the_file = open(file_name, "w")

        for key, val in data.items():
            the_file.write(str(key) + ", " + val + "\n")
    finally:
        the_file.close()


def write_list(file_name, the_list, prop):
    try:
        the_file = open(file_name, "w")

        for item in the_list:
            the_file.write(getattr(item, prop) + "\n")
    finally:
        the_file.close()