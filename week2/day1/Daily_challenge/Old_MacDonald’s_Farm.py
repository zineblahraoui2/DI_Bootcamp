class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, **kwargs):
        for animal, amount in kwargs.items():
            if animal in self.animals:
                self.animals[animal] += amount
            else:
                self.animals[animal] = amount

    def get_info(self):
        print(f"{self.name}'s farm")
        for animal, amount in self.animals.items():
            print(f"{animal} : {amount}")
        print("E-I-E-I-O")

    def get_animal_types(self):
        return sorted(self.animals.keys())  # returns a list

    def get_short_info(self):
        types = ", ".join(self.get_animal_types())
        print(f"{self.name}'s farm has {types}.")

    
object_Farm = Farm("peas")

object_Farm.add_animal(cow=2)
object_Farm.add_animal(cow=4)
object_Farm.add_animal(bird=5)
object_Farm.add_animal(dog=5)

object_Farm.get_info()
print(object_Farm.get_animal_types())
object_Farm.get_short_info()
object_Farm.add_animal(cow=5, sheep=2, goat=12)
object_Farm.get_info()
      