month = int(input("Enter a month number (1–12)"))
if month in range(3,6): # test each condition
    print("The season is Spring ")
elif month in range(6,9): # elif test only if the previous conditions are false
    print("The season is Summer ")   
elif month in range(9,12):
    print("The season is Autumn ") 
else:
    print("The season is Winter ")     
    

