def palindrome_checker(number):
    #for i in range(number,number+1):
        count = 0
        len_num = len(str(number))
        pairs = len_num // 2
        if pairs == 0:
            pairs = len_num%2
        for j in range(1,pairs+1):
            if str(number)[j-1] == str(number)[-j]:
                count+=1
            if count == pairs:
                return True
        return False
def algorithm_196(number):
    count = 0
    while count<60:
        number = number + int(str(number)[::-1])
        if palindrome_checker(number):
            return True
        count+=1
    return False

def main():
    palindrome = 0
    integer_1= int(input("Integer 1: "))
    integer_2 = int(input("Integer 2: "))
    non_lycherel = 0
    lycherel = 0
    for i in range(integer_1,integer_2+1):
        if palindrome_checker(i):
            palindrome+=1
        elif palindrome_checker(i)== False:
            if algorithm_196(i):
                non_lycherel+=1
            else:
                lycherel +=1
                print(f"{i} is probably lycherel")
    print(f"Palindrome numbers = {palindrome}")
    print(f"Not lycherel numbers = {non_lycherel}")
    print(f"Lycherel = {lycherel}")
main()