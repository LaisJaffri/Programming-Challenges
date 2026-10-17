#string = input("Enter a two character string: ")
string = input("Enter a two character string: ")
while len(string)!=2:
    string = input("Enter a two character string: ")
binary = ""
for i in range(2):
    n = ord(string[i])
    binary += format(n,"08b")
integer = int(binary,2)
print(f"As a bit pattern: {binary}")
print(f"As an integer: {integer}")