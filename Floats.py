import numpy as np
list_of_numbers =[]
for number in np.arange(1.5,5.5,0.5):
    if number.is_integer():
        list_of_numbers.append(int(number))
    else:
        list_of_numbers.append(number)

print(list_of_numbers)




