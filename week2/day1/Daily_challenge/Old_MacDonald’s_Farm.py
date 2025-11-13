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
        print("   E-I-E-I-0!")
    
    def get_animal_types(self):
        dict_keys = list(self.animals.keys())
        dict_keys.sort()
        return dict_keys
        
    def get_short_info(self):
        list_of_animals = self.get_animal_types()
        string_of_animals = " ".join(list_of_animals)
        last_word = string_of_animals.split()[-1]
        before_and_word = string_of_animals.split()[-2]
        print(f"{self.farm_name} farm has {before_and_word} and {last_word}")
        

object_Farm = Farm("peas") 
object_Farm.add_animal('cow',2)
object_Farm.add_animal('cow',4)
object_Farm.add_animal('bird',5)
object_Farm.add_animal('dog',5)
object_Farm.get_info()
print(object_Farm.get_animal_types())
object_Farm.get_short_info()

      