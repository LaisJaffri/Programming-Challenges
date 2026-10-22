string = "My Rabbit"
new = sorted(string.upper().replace(" ", ""))
new_phrase = ""
for char in new:
    new_phrase+=char
print(new_phrase)
