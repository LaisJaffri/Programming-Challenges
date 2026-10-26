first = "NINE"
second = "ELEPHANT"
letters = []
for char in first:
    letters.append(char)
count = 0
for let in letters:
    if let in second:
        second = second.replace(let,"",1)
        count+=1
if count == len(first):
    print("Can be made")
else:
    print("Cannot be made")