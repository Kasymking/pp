import string

for letter in string.ascii_uppercase:
    file = f"{letter}.txt"
    with open(file,'w') as f:
        f.write(file)