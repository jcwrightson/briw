class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Drink:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Preference:
    def __init__(self, person, drink):
        self.person = person
        self.drink = drink

    def __str__(self):
        return self.person.__str__() + "\t" + self.drink.__str__()


class Round:
    def __init__(self):
        self.active = False
        self.order = []

    def add_to_order(self, person, drink):
        if self.active == True:
            self.order.append(Preference(person, drink))

    def set_active(self, status):
        self.active = status
