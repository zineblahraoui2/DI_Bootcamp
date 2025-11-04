3 <= 3 < 9 # True
3 == 3 == 3 # True
bool(0) # False
bool(5 == "5") # False
bool(4 == 4) == bool("4" == "4") # True
bool(bool(None)) # False

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10
print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)