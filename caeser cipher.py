text = "Hello, World!"

shift = 3
caeser = ""
for char in text:
    if 65<=ord(char)<=90 or 97<=ord(char)<=122:
            if (ord(char)+shift)>122:
                caeser+=chr(ord(char)-26+shift)
            elif (ord(char)+shift)>90 and ord(char)<97:
                caeser+=chr(ord(char)-26+shift)
            else:
                caeser+=chr(ord(char)+shift )
    else:
        caeser+=char
print(caeser)