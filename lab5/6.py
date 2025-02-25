import re

with open('row.txt','r') as file:
    text = file.read()

pattern = '[ ,.]'

result = re.sub(pattern, ':', text)
print(result)