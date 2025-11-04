list_of_numbers =[]
start =1.5
step = 0.5
stop = 5
while (start <= stop):
    if start.is_integer():
        list_of_numbers.append(int(start))
    else:
        list_of_numbers.append(start)
    start =start + step
print(list_of_numbers)





