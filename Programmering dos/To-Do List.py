import os

folderPath = "C:/Users/EliasAdestam/PycharmProjects/Programmering dos" #Användarfilväg
files = os.listdir(folderPath)
txtFiles = [f for f in files if f.endswith('.txt')]

print("Welcome to your to-do list! Select existing to-do list below or create a new one:")

def fileDisplay(txtFiles):
    for txtFiles in txtFiles:
        print(txtFiles[:-4])
    return txtFiles
def fileExplore():
    fileName = input("Please enter the name of the file you want to edit or create: ")
    filePath = os.path.join(folderPath, fileName)
    return filePath
filePath = fileExplore()

if os.path.exists(filePath):
    fileExists = True
    fileCreate = "no"
    file = open(filePath, "r+")
    tasks = input("Please enter your tasks here: \n")
    file.write(tasks)
    print("Tasks added to the file.")
else:
    fileExists = False
    fileCreate = input("The list could not be located. Would you like to create one? (yes/no) ").lower()

if fileCreate == "yes" and fileExists == False:
    print("Please enter your tasks: ")
    file = open(filePath, "w")
    tasks = input()
    file.write(tasks)
elif fileCreate == "no" and fileExists == False:
    print("Okay, try to search for your file again")
    fileDisplay()
    fileExplore()
elif fileExists == False:
    print("Unable to understand prompt! ")

if 'file' in locals():
    file.close()