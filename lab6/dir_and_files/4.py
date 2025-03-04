with open('test.txt') as file:
    cnt = 0
    for i in file:
        cnt += 1

print("The number of lines:", cnt)