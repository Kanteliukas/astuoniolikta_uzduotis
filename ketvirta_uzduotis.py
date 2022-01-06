from operator import attrgetter
import random

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"({self.name} - {self.age})"

def reverse_sorting(people):
    return people[::-1]

def main():
    printable_list = []
    names = ["Mantvydas", "Karolina", "Benas", "Orinta", "Katažina", "Mikas"]
    man = Human("Jonas", 36)
    woman = Human("Jadvyga", 24)
    people = [
        Human(f"{name}", random.randint(20, 50))
        for name in names
    ]
    people.extend([man, woman])

    printable_list.extend([
        people,
        sorted(people, key=attrgetter("name")),
        sorted(people, key=attrgetter("age")),
        reverse_sorting(people)
    ])

    for sorted_list in printable_list:
        print(sorted_list)

main()
