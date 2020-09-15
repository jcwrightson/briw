def print_list(the_list):
    for item in the_list:
        print(item)


def get_countries():

    with open("countries.csv", "r") as the_file:
        lines = the_file.readlines()
        for line in lines:
            data.append(line)

    return data


def print_countries():
    countries = get_countries()
    print_list(countries)
    return countries
