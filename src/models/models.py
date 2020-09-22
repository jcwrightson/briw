class Person:
    def __init__(self, id, forename, surname, drink_id=None):
        self.forename = forename
        self.surname = surname
        self.id = id
        self.drink_id = drink_id

    def __str__(self):
        return f"{self.id} \t {self.forename} {self.surname} \t {self.drink_id}"


class Drink:
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.id} \t {self.name} \t\t £{self.price}"


class Preference:
    def __init__(self, person, drink):
        self.person = person
        self.drink = drink

    def __str__(self):
        return f"{self.person.forename} {self.person.surname} \t\t {self.drink.name}"


class Round:
    def __init__(self, order={}):
        self.active = False
        self.order = order

    def add_to_order(self, person: Person, drink: Drink):
        if self.active == True:
            self.order[person] = drink

    def set_open(self, buyer: Person):
        self.active = True
        self.buyer = buyer

    def set_closed(self):
        self.active = False

    def clear_order(self):
        self.order = {}

    def print_order(self):

        total = len(self.order)

        if total == 0:
            print("Empty")
            return

        print(f"Buyer: {self.buyer.name}")
        print("Name\tDrink")

        for person, drink in self.order.items():
            print(person.name, "\t", drink.name)

        if total == 1:
            print(f"{total} item")
        else:
            print(f"{len(self.order)} item(s)")
