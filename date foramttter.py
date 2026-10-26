import datetime
date = "31/02/2027"
day,month,year= date.split("/")
months = ["offset","January","February","March","April","May","June","July","August","September","October","November","December"]
month_name = months[int(month)]
try:
    proper = datetime.date(int(year),int(month),int(day))
    day_name = proper.strftime("%A")
    print(f"{day_name} {day} {month_name} {year}")
except ValueError:
    print("Not a Valid Date") 
