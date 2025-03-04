import os

file_path = input("Enter file path to delete: ")

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):  # Проверяем, можно ли удалить файл
        os.remove(file_path)
    else:
        print("You don't have permission to delete this file")
else:
    print("The file does not exist.")