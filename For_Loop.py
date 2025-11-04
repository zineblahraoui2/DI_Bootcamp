numbers = []
for number in range(1,21):
    numbers.append(number)
print(numbers) 
for i in range(len(numbers)-1):
    if i % 2 == 0:
         print(f"Index {i} -> Value {numbers[i]}")
        
