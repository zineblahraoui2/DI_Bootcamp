total_cost = 0
ages = []

while True:
    age_input = input("Enter the age of a family member (or type 'done' to finish): ")

    if age_input.lower() == "done":
        break
    
    age = int(age_input)
    ages.append(age)

    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    total_cost += ticket_price

print("\nFamily ages:", ages)
print("Total cost of the tickets: $", total_cost)
