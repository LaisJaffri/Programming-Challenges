import datetime
day = int(input("What day is your birthday?: "))
month = input("What month is your birthday?: ")
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
for j in range(12):
    if month == months[j]:
        month = j+1
today = datetime.date.today()
today_month = today.month
if month<today_month:
    birthday_year = today.year+1
else:
    birthday_year = today.year
birthday = datetime.date(birthday_year,month,day)
diff = (birthday-today).days
if diff == 0:
    print(f"Today is the {today}, Happy Birthday!!!")
else:
    print(f"Your birthdat is in {diff} days")
