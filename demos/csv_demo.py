import csv


class User:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f"I'm {self.name} and i'm {self.age} years young, and i'm {self.height}cm"


name = input("Please enter name: ")
age = input("Please enter age: ")
height = input("Please enter height: ")

new_user = User(name, age, height)

users = []
users.append(new_user)

def save():
    try:
        with open("users.csv", "a", newline="\n") as the_file:
            writer = csv.writer(the_file)

            for user in users:

                writer.writerow([user.name, user.age, user.height])
    except FileNotFoundError:
        print("File not found")

with open("users.csv", "r") as the_file:
    reader = csv.reader(the_file)

    for row in reader:

        saved_user = User(row[0], row[1], row[2])
        print(saved_user)
