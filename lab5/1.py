import re 

with open(r'C:\Users\Касымжомарт\Desktop\pp\lab5\row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

pattern = 'ab*'
result = re.findall(pattern,text)

print(result)