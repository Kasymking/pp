import re

with open(r'C:\Users\Касымжомарт\Desktop\pp\lab5\row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

pattern = '[ ,.]'

result = re.sub(pattern, ':', text)
print(result)