string = "horse"
swapped = ""
vowels = ["a","e","i","o","u"]
vowels_in_string = []
for char in string:
    if char in vowels:
        vowels_in_string.append(char)
vowels_in_string.reverse()
for i,char,j,vowel in zip(enumerate(string,vowels_in_string)):
    if char in vowels:
        swapped+=vowels_in_string[j]
    else:
        swapped+=char
print(swapped)

"""       
print(vowels_in_string)
for i in range(len(vowels_in_string)//2):
    string = string.replace(vowels_in_string[i],vowels_in_string[-(i+1)],1)
    string = string.replace(vowels_in_string[-(i+1)],vowels_in_string[i],1)
print(string)
"""