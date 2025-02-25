import re

with open('row.txt','r') as file:
    text = file.read()

pattern = '[a-z]_[a-z]'
result = re.findall(pattern,text)

print(result)