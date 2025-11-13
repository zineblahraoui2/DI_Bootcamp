class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat_1 = Cat("Selina", 2)
cat_2 = Cat("Lina", 4)
cat_3 = Cat("Verona", 1)

def find_oldest_cat(cat_1, cat_2, cat_3):
    cats_old_ages = [cat_1, cat_2, cat_3]
    oldest_cat = max(cats_old_ages, key=lambda cat: cat.age)
    return oldest_cat

oldest = find_oldest_cat(cat_1, cat_2, cat_3)
print(f"The oldest cat is {oldest.name}, aged {oldest.age}")


  