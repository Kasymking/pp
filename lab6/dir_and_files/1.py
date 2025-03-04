import os 

current_dir = os.getcwd()

print("Only directories: ")
for entry in os.scandir(current_dir):
    if entry.is_dir():
        print(entry.name)

print('-' * 50)
print("Only files:")
for entry in os.scandir(current_dir):
    if entry.is_file():
        print(entry.name)

print('-' * 50)
print("All directories and files:")
for entry in os.scandir(current_dir):
    print(entry.name)
    