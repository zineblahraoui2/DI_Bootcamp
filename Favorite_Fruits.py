Fruits = input("Write your favorite fruits")
fruits_list = Fruits.split()
print("Your favorite fruits are:", fruits_list)
Fruit = input("Write any fruit")
if Fruit in fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")    