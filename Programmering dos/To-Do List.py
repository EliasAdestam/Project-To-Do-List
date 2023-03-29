import os

folderPath = "C:/Users/EliasAdestam/PycharmProjects/Programmering dos"
files = os.listdir(folderPath)
txtFiles = [f for f in files if f.endswith('.txt')]

print("Welcome to your to-do list! Select existing to-do list below or create a new one:")

for txtFiles in txtFiles:
    print(txtFiles)


file = open("Todolist_1.txt", "a")
file.write(input("Please enter your tasks here: "))
