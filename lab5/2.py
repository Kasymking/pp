import re

with open('row.txt', 'r') as file:
    text = file.read()

pattern = 'ab{2,3}' # abbb abbbb
result = re.findall(pattern,text)

print(result)