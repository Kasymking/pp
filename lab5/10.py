import re

text = "AaaBbbCccDddEee!FffGogi."

pattern = '[A-Z][^A-Z]*'
process = re.findall(pattern, text)

My_list = [i.lower() for i in process]

print('_'.join(My_list)) 