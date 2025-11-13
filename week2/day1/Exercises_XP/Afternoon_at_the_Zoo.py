class Zoo :
    def __init__(self,zoo_name):
        self.animals = []
        self.zoo_name = zoo_name

    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"{new_animal} est déjà dans le zoo")    

    def get_animals(self):
        for animal in self.animals:
            animal
    def sell_animal(self,animal_sold):
        for animal in self.animals:
            if animal_sold is animal:
                self.animals.remove(animal)

    def sort_animals(self):
        self.animals.sort()
        dict_of_animals ={}
        for i,value in enumerate(self.animals,start= 0):
            key_carachter = chr(ord(("a"))+i)
            dict_of_animals[key_carachter] = value
        grouped_animals = {}
        for key_carachter in dict_of_animals:
            first_letter = dict_of_animals[key_carachter][0].lower()
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = [dict_of_animals[key_carachter]]
            else:
                grouped_animals[first_letter].append(dict_of_animals[key_carachter])

        return grouped_animals        
        

    def get_groups(self):
        groups = self.sort_animals()
        return groups
    

zoo_object = Zoo("ATLAS")
zoo_object.add_animal("Dog")
zoo_object.add_animal("bird")
zoo_object.add_animal("cat")
zoo_object.add_animal("cat")
zoo_object.add_animal("bear")
zoo_object.get_animals()
zoo_object.sell_animal("Dog")
zoo_object.sort_animals()
print(zoo_object.get_groups())