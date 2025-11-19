from Dogs import Dog
import random
class PetDog(Dog):
    def __init__(self, name, age, weight,trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.trained = True
        return self.bark() 
    
    def play(self,*dogs):
        dog_names = [self.name for dog in dogs]
        return f"{dog_names}all play together"

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            random_trick = random.choice(tricks) 
            print(random_trick)
            print(tricks.index(random_trick))
               
    
dog1 = PetDog("Rex",2,6)  
dog2 = PetDog("dogy",5,8)  
dog3 = PetDog("dodi",6,8) 
dog1.train()
dog1.play("Boby","koki")
dog1.do_a_trick()

