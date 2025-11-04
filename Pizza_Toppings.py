toppings = []
base_price = 10
topping_price = 2.50

while True:
    topping = input("Enter a pizza topping (or type 'quit' to stop): ").lower()
    if topping == "quit":
        break
    
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_cost = base_price + (len(toppings) * topping_price)

print("\nYour pizza toppings are:", toppings)
print(f"Total cost: ${total_cost:.2f}")
