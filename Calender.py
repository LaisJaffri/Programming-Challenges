day = input("Enter the first day of the month: ")
while True:
    day = input("Enter the first day of the month: ")
    if len(day)==3:
        break
total_days = int(input("Enter the total number of days in the month: "))
days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
print("".join(f"{x:>4}" for x in days))
# print(" ".join(str(x) for x in days)). This was printing out what you wanted unformatted to how we wanted to formate our own dates
count = days.index(day)+1
print(f"{" "*((count-1)*4)}",end = "")
for date in range(1,total_days+1):
    if count<=7:
        print(f"{date:>4}",end="")
    else:
        print()
        print(f"{date:>4}",end="")
        count = 1
    count+=1