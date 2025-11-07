family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total = 0
for name,age in family.items():
    if age < 3 :
        price = 0
        print(f"The price is Free {0}")
    elif 3<= age <= 12:
        price = 10
        print(f"the ticket price {10}")
    else: 
        price = 15
        print(f"the ticket price {15}")
    total += price 
    print(total)   




    