users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
dict_1 = {}
for i,user in enumerate(users):
    dict_1[user]= i
print(dict_1)
dict_2 ={}
for i,user in enumerate(users):
    dict_2[i]=user
print(dict_2)  
dict_1 = {}
for i,user in enumerate(sorted(users)):
    dict_1[user]= i
print(dict_1)  
 