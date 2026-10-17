number_1 = int(input("Enter a number between 10 and 49: "))
while number_1<10 and number_1>49:
    number_1 = int(input("Enter a number between 10 and 49: "))
factor = 99 - number_1
number_2 = int(input("Enter a number between 50 and 99: "))
while number_2<50 and number_2>99:
    number_2 = int(input("Enter a number between 10 and 49: "))
total = number_2 + factor
hundred = int(str(total)[0])
units = (int(str(total)[1])*10) + (int(str(total)[2]))
print(number_2 - (units+hundred))

