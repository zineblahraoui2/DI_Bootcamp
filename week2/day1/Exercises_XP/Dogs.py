class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name} goes woof!")  

    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x} cm high!") 

def comparing_height_of_dogs(dog1, dog2):
    height_dogs = [dog1, dog2]
    comparison = max(height_dogs, key=lambda dog: dog.height)
    return comparison

davids_dog = Dog("REX", 10)    
sarahs_dog = Dog("FOX", 40)

if davids_dog.height == sarahs_dog.height:
    print("They have the same height")
else:    
    heigher = comparing_height_of_dogs(davids_dog, sarahs_dog)
    print(f"The taller dog is {heigher.name} with {heigher.height} cm")

print(davids_dog.name)
print(davids_dog.height)
print(sarahs_dog.name)
print(sarahs_dog.height)
davids_dog.bark()
sarahs_dog.jump()


    