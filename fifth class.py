import datetime

day = int(input("Zadej den tveho narozeni: "))
month = int(input("Zadej mesic tveho narozeni: "))
year = int(input("Zadej rok tveho narozeni: "))

date_of_birth = datetime.datetime(year, month, day)
format = str(date_of_birth.day)+ "/" +str(date_of_birth.month)+ "/" +str(date_of_birth.year)
print(format)



