phrase = input("Enter a word or phrase: ")
phrase = phrase.upper().replace(" ","")
#phrase = phrase.replace(" ", "")
for char in phrase:
    #if ord(char)<65 or ord(char)>91:
    if not(char.isupper()):
        phrase = phrase.replace(char, "")
print(phrase)
reversed = phrase[::-1]
if phrase == reversed:
    print("Palindrome")
else:
    print("Not a palindrome")
    
