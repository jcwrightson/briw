def read_data(file_name):

    data = {}

    try:
        the_file = open(file_name, "r")
        lines = the_file.readlines()

        for line in lines:  # '0, Beer'
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
