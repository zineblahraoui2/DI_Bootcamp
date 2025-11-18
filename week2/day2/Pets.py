class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def walk(self):   
        return f"{self.name} is just walking around" 
    
class Siamese(Cat):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color    

class Pets:
    def __init__(self,animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

bengal_obj = Cat("RIMI",4)
chartreux_obj = Cat("RIRI",3)
siamese_obj = Siamese("ROSA",4,"brown")
all_cats = [bengal_obj, chartreux_obj, siamese_obj]
sara_pets = Pets(all_cats)
sara_pets.walk()

