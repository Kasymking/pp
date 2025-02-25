import re

with open('row.txt','r') as file:
    text = file.read()

pattern = '[A-Z][a-z]+'

result = re.findall(pattern,text)

print(result)