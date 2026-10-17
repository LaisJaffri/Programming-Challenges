import math
age = int(input("Enter an age:  "))
day = input("Enter a day:  ")
under_12 = 6.5
discount = 0.8
between_12_17 = 8.00
adults = 11.00
over_65 = 7.50
if age<12:
    price = under_12
elif 12<=age<=17:
    price = between_12_17
elif 17<age<65:
    price = adults
else:
    price = over_65
if day == "Tuesday":
    price *= discount
#price = math.trunc(price*(10**2))
#price /= 10**2
print(f"{price:.2f}")