""" 
    with open('example.py','rb') as s, open('example1.py','wb') as d:
    d.write(s.read())
    для копирование любых типов файлов (.txt,.py,.exe,.jpg)
"""

with open('test.txt','r') as s, open('copy.txt','w') as d:
    d.write(s.read())