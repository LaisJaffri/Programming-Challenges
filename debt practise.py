import math
def FindRepayment(debt,interest,month,repayment,minimum):
    final = 0
    count = 0
    while debt>0:
        debt = debt * interest
        if (debt*repayment)>minimum:
            debt = debt*repayment
            final = final + debt
        elif debt>minimum:
            debt = debt - minimum
            final = final + minimum
        else:
            final = final + debt
            debt = debt - debt
        count +=1
        if month =="Y":
            print(count," and you paid off ",final)
        else:
            print(math.ceil(final*100)/100," and ",math.ceil(debt*100)/100)
def main():
    debt = float(input("Enter debt amount: "))
    interest = float(input("Enter interest amount: "))
    interest = 1 +(interest/100)
    month = input("Do you want to see how many monthly payments you need? Y for Yes: ")
    repayment = float(input("What is the repayment percentage you want?: "))/100
    minimum = float(input("What is the minimum amount for repayment?: "))
    FindRepayment(debt,interest,month,repayment,minimum)
main()