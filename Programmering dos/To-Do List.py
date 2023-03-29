import os

folderPath = "C:/Users/EliasAdestam/PycharmProjects/Programmering dos"
files = os.listdir(folderPath)
txtFiles = [f for f in files if f.endswith('.txt')]

print("Welcome to your to-do list! Select existing to-do list below or create a new one:")

for txtFiles in txtFiles:
    print(txtFiles)

fileName = input("Please enter the name of the file you want to edit or create: ")
filePath = os.path.join(folderPath, fileName)

fileCreate = ""

if os.path.exists(filePath):
    file = open(filePath, "a")
else:
    open(fileName, "a").close

if fileCreate == "YES":
    file.write(input("Please enter your tasks here: "))
    file.close()
else:
    fileCreate = input("The list could not be located. Would you like to create one? (yes/no) ").lower()

if fileCreate == "yes":
    print("Please enter your tasks: ")
    file = open(filePath, "w")
elif fileCreate == "no":
    print("Okay, try to search for your file again")
else:
    print("Unable to understand prompt! ")