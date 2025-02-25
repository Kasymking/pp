import re 

with open('row.txt','r') as file:
    text = file.read()

pattern = 'ab*'
result = re.findall(pattern,text)

print(result)