class Person:
    def __init__(self, name):
        self.name = name


class Drink:
    def __init__(self, name):
        self.name = name


class Preference:
    def __init__(self, person, drink):
        self.person = person
        self.drink = drink


class Round:
    def __init__(self):
        self.active = False
        self.order = []

    def add_to_order(self, person, drink):
        if self.active == True:
            self.order.append(Preference(person, drink))

    def set_active(self, status):
        self.active = status