first_roman_num = "XLIV"
second_roman_num = "CCLXV"
roman_to_dec = {
    "I":1,
    "V": 5,
    "X":10,
    "L":50,
    "C":100
}
def converter_to_decimal(roman_num,roman_to_dec):
    total = 0
    keys = list(roman_to_dec)
    bigger = False
    for i in roman_num:
        for roman_letter in roman_to_dec:
            if roman_num.find(i)+1 < len(roman_num):
                next_letter = roman_num[roman_num.find(i)+1] 
            if i == roman_letter and roman_to_dec[next_letter]>roman_to_dec[roman_letter]:
                total+=(roman_to_dec[next_letter]-roman_to_dec[roman_letter])
                bigger = True
            elif i == roman_letter and bigger == False:
                total+=roman_to_dec[roman_letter]
                bigger = False
    return total

def converter_to_roman(test,roman_to_dec):
    num = len(str(test))
    roman = ""
    """
    if num==3:
        roman+="C"*(test//100)
        num = 2
        test = test - ((test//100)*100)
        print(test)
    if num == 2:
        roman+="X"*(test//10)
        num = 1
    """
    for letter in roman_to_dec:
        if roman_to_dec[letter]==test:
            test = test - roman_to_dec[letter]
            print(letter)
    print(roman)


number1 = converter_to_decimal(first_roman_num,roman_to_dec)
number2 = converter_to_decimal(second_roman_num,roman_to_dec)
total = number1 + number2
test = 250
converter_to_roman(test,roman_to_dec)