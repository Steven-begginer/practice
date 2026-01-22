import random
# new version of writing class with decorators.
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

Hat.sort("Harry")
