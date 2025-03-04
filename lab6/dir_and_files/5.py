lst = ["hello" , "My name is" , "Jones" , "And", "I'm student"]

with open('text.txt','w') as file:
    for i in lst:
        file.write(i + '\n')