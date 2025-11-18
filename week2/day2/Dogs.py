class Dog:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f" {self.name} is barking"
    
    def run_speed(self):
        return self.weight / self.age*10

    def fight(self,other_dog):  
        self_dog = self.run_speed()*self.weight
        other_dog = other_dog.run_speed()*other_dog.weight 

        if self_dog > other_dog:
            return f"{self.name} won the fight"
        elif self_dog < other_dog:
            return f"{other_dog.name} won the fight"
        else:
            return "its equal"
    
dog1 = Dog("Rex",4,10)  
dog2 =  Dog("RIMI",5,6)  
print(dog1.bark())
print(dog1.run_speed())
print(dog2.run_speed())
print(dog1.fight(dog2))