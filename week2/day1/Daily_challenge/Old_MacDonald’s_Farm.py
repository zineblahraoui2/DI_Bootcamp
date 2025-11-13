class Farm:
    def __init__(self,farm_name):
        self.farm_name = farm_name
        self.animals = {}

    def add_animal(self,animal_type,count=1): 
            if animal_type  in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count
            return self.animals    
             
    def get_info(self):
        print(f"{self.farm_name}\n")
        for animal_type,count in self.animals.items():
            print(f"{animal_type}:{count}") 

object_Farm = Farm("Happiness") 
object_Farm.add_animal('cow', 2)
object_Farm.add_animal('cow', 4)
object_Farm.get_info()

      