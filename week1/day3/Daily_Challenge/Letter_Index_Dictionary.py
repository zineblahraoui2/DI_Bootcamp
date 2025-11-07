word = input("enter a word")
dict_1 = {}
for i,letter in enumerate(word):
    if letter in dict_1:
        dict_1[letter].append(i)  
    else:
        dict_1[letter]=[i]
print(dict_1)    
