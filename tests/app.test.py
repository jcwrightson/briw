from classes import Person, Drink, Preference
from app import create_pref, create_person


def test_create_pref():

    prefs = {}

    test_person = Person(0, "Test")

    test_drink = Drink(0, "Test Brew")

    expected_output = Preference(test_person, test_drink)

    actual_output = create_pref(test_person, test_drink, prefs)

    # assert expected_output == actual_output.__dict__

    assert len(prefs) == 1


def test_create_person():

    people = {}

    expected = Person(0, "John")

    actual = create_person("John", 0, people)

    assert expected.__dict__ == actual.__dict__


tests = [test_create_pref, test_create_person]

for test in tests:
    test()
