class Person:
    def __init__(self,first_name,age,last_name=""):
        self.first_name =first_name  
        self.age = age
        self.last_name = last_name

    def is_18(self):  
        if self.age >= 18: return True ; return False  

class Family:
    def __init__(self,last_name):
        self.last_name = last_name
        self.members = []


    def born(self,first_name, age):
        new_person = Person(first_name,age)
        new_person.last_name = self.last_name
        return self.members.append(new_person)

    def check_majority(self,first_name):
        for person in self.members:
            if person.first_name == first_name:
                if  self.age > 18:
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                print("Sorry, you are not allowed to go out with your friends.")    
                
    def family_presentation(self):
        return self.last_name
    

   

