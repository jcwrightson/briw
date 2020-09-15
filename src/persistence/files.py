import csv


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

    with open(file_name, "w", newline="\n") as csvfile:

        writer = csv.writer(csvfile)

        for row in rows.values():

            writer.writerow(build_row(row))


def write_prefs(file_name: str, prefs: dict):

    with open(file_name, "w", newline="\n") as csvfile:

        writer = csv.writer(csvfile)

        for pref in prefs.values():

            writer.writerow([pref.person.id, pref.drink.id])


def read_data_as_dict():
    data = {}
    with open("names.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.update({row["uid"]: row})
    return data


def write_data_as_dict(the_dict, fieldnames):
    with open("names.csv", newline="", mode="w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in the_dict:
            writer.writerow(row)


def get_field_names(the_dict):
    key = list(the_dict.keys())[0]
    record = the_dict.get(key)
    return list(record.keys())
