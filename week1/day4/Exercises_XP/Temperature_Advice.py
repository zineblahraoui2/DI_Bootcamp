import random
month = int(input("Enter a month from 1 to 12"))
def get_random_temp():
    if  month in [12,1,2]:
        print("the season is Winter")
        return random.uniform(-10,10)  
    elif month in [3,4,5]:
        print("the season is Spring") 
        return random.uniform(20,30) 
    elif month in [6,7,8]:
        print("the season is Summer")
        return random.uniform(30,40) 
    elif month in [9,10,11]:
        print("the season is Autumn") 
        return random.uniform(10,20) 

def main():
    temperature_value = get_random_temp()
    print(f"The temperature right now is {temperature_value} degrees Celsius.")
    if temperature_value < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temperature_value < 16:
        print("Quite chilly! Don’t forget your coat.")  
    elif 16 <= temperature_value < 23:
        print("Nice weather.")    
    elif 24 <= temperature_value < 32:
        print("A bit warm, stay hydrated.") 
    elif 32 <= temperature_value <= 40:
        print("It’s really hot! Stay cool.")    

main()