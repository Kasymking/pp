import re

with open(r'C:\Users\Касымжомарт\Desktop\pp\lab5\row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

pattern = '[a-z]_[a-z]'
result = re.findall(pattern,text)

print(result)