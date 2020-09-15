import csv
import uuid

from helpers import read_rows


class Person:
    def __init__(self, fname, lname, age):
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.uid = str(uuid.uuid4())


def read_data_as_dict():
    data = {}
    with open('names.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.update({row['uid']: row})
    return data


def write_data_as_dict(the_dict, fieldnames):
    with open('names.csv', newline='', mode='w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in the_dict:
            writer.writerow(row)


def get_field_names(the_dict):
    key = list(the_dict.keys())[0]
    record = the_dict.get(key)
    return list(record.keys())


def create_person(the_dict, first_name, last_name, age):
    new_person = Person(first_name, last_name, age)
    the_dict.update({new_person.uid: new_person.__dict__})
    return new_person


names_dict = read_data_as_dict()


# write_data_as_dict(names_dict.values(), get_field_names(names_dict))


def create_person(name, the_list):
    if name != "" and type(name) != int:
        the_list.append(name)

    return the_list


def test_create_person_adds_one_item():

    name = "Test Person"
    the_list = []
    expected = ["Test Person"]

    actual = create_person(name, the_list)

    assert expected == actual


def test_create_person_doesnt_add_empty():

    name = ""
    the_list = []
    expected = []

    actual = create_person(name, the_list)

    assert expected == actual


def test_create_person_doesnt_add_numeric_name():

    name = 122334
    the_list = []
    expected = []

    actual = create_person(name, the_list)

    assert expected == actual
