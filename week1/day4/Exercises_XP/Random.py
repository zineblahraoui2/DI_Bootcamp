import random
def generate_random_numbers(number):
    Random_number = random.randint(1, 100)
    if Random_number == number:
        print("Success!")
    else:
        print(f"Fail! Your number:{number} , Random number:{Random_number}")    

generate_random_numbers(int(input("Enter a number between 1 and 100: ")))