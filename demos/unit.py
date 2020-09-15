def sum(x, y):
    return x + y


def test_sum_adds_two_numbers():
    # 1. Assemble
    # 2. Act
    # 3. Assert

    a = 1
    b = 2
    expected = 3

    actual = sum(a, b)

    assert expected == actual


test_sum_adds_two_numbers()


def create_item(name, the_list):
    data = the_list
    if name != "" and type(name) != int:
        data.append(name)
    return data


def test_create_item_adds_one():

    name = "Bilan"
    data = []
    expected = ["Bilan"]

    actual = create_item(name, data)
    assert expected == actual


def test_create_item_rejects_empty():

    name = ""
    data = []
    expected = []

    actual = create_item(name, data)
    assert expected == actual


def test_create_item_rejects_ints():

    name = 1234
    data = []
    expected = []

    actual = create_item(name, data)

    assert expected == actual

test_create_item_adds_one()
test_create_item_rejects_empty()
test_create_item_rejects_ints()
