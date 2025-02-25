import re

text = "aaa_ccc_bbb_hello!_privet."


pattern = r'_'
alist = re.split('_',text)

cap_list = []

for i in alist:
    i = i.capitalize()
    cap_list.append(i)

for i in cap_list:
    print(i, end='')