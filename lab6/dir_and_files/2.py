import os

path = (input("Enter the directory path: "))

print(os.access(path,os.F_OK))
print(os.access(path,os.R_OK))
print(os.access(path,os.W_OK))
print(os.access(path,os.X_OK))

#C:\Users\Касымжомарт\Desktop\pp\lab6\dir_and_files\copy.txt