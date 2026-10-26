string = "My Rabbit"
string_change= string.replace(" ", "").upper()
sort = ""
sorted_string = ""
while string_change != "":
    sort+=min(string_change)
    string_change = string_change.replace(min(string_change),"",1)
for sorted in sort:
    if sorted in string:
        sorted_string+=sorted
        string = string.replace(sorted,"")
    elif sorted.lower() in string:
        sorted_string+=sorted.lower()
    else:
        sorted_string+=sorted
print(sorted_string)
