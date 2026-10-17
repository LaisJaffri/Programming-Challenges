while True:
    number = int(input("Enter a number: "))
    if number>0:
        break
def increasing(number):
    count = 1
    num = str(number)
    before = num[0]
    for digit in num[1:]:
        if int(digit)>=int(before):
            count+=1
        before = digit
    if count == len(num):
        return True
    else:
        return False
def decreasing(number):
    count = 1
    num = str(number)
    before = num[0]
    for digit in num[1:]:
        if int(digit)<=int(before):
            count+=1
        before = digit
    if count == len(num):
        return True
    else:
        return False
def perfect_bouncy(number):
    increases = 0
    decreases = 0
    num = str(number)
    before = num[0]
    for digit in num[1:]:
        if int(digit)>int(before):
            increases+=1
        elif int(digit)<int(before):
            decreases+=1
        before = digit
    if increases == decreases:
        return True
    return False
if not(increasing(number)) and  not(decreasing(number)):
    if perfect_bouncy(number):
        print("perfectly bouncy")
    else:
        print("bouncy")
else:
    print("not bouncy")