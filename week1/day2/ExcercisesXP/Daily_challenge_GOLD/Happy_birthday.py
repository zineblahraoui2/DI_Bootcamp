birthdate = input("Write your birthday in the specified format: DD/MM/YYYY")
year = birthdate.split("/")[-1]
print("Year:", year)
carrent_year = 2025
year = int(year)
age = carrent_year - year
number_of_candles = age % 10 
cake = "    ___"+number_of_candles*"i"+"___\n"+"   |:H:a:p:p:y:|  \n" + " __|___________|__\n" +"|^^^^^^^^^^^^^^^^^|\n" +"|:B:i:r:t:h:d:a:y:|\n" + "|                 |\n"+ "~~~~~~~~~~~~~~~~~~~\n"
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(cake*2)
else:
    print(cake)