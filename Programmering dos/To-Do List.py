import os
import shelve
def getTxtFilesInFolder(folderPath):                   #Visar .txt filerna i valda directory
    files = os.listdir(folderPath)
    return [f for f in files if f.endswith('.txt') and f != "directoryPath.txt"]

def getFilePath(folderPath, fileName):   #Hittar specifika filers platser i directory
    return os.path.join(folderPath, f"{fileName}.txt")

def readTasksFromFile(filePath):  #Öppnar och läser specifika filers innehåll
    with open(filePath, "r") as f:
        tasks = f.readlines()
    return tasks

def createOrOpenFile(filePath, createFile=False):     #Ändrar existerande filer och skapar nya filer om den inte finns
    if os.path.exists(filePath):
        mode = "a"
    elif createFile:
        mode = "w"
    else:
        return None
    return open(filePath, mode)

def removeTask(filePath, taskIndex):              #Tar bort to-do grejer i själva To-Do-Listen
    tasks = readTasksFromFile(filePath)

    if taskIndex < 1 or taskIndex > len(tasks):
        print("Invalid task index.")
        return

    task = tasks.pop(taskIndex - 1)

    with open(filePath, "w") as f:
        f.writelines(tasks)

    print(f"Task '{task.strip()}' removed from the file.")

def directoryConfig():                  #Kommer ihåg vald katalog av användaren
    db = shelve.open("ToDoListConfig")
    if not db:                          #Kollar om det finns en lagrad värde
        directoryPath = input("Enter the directory where you want your lists to be saved here: ")
        db["directoryPath"] = directoryPath
    else:
        directoryPath = db['directoryPath']
        print(f"The current directory path is {directoryPath}")

    changeDirectory = input("Would you like to change the directory path? (yes/no): ")  #Om det finns ett lagrat värde kollar den med användaren om den vill byta
    if changeDirectory.lower() == 'yes' or changeDirectory.lower() == 'y':
        directoryPath = input("Please enter a directory where you want to have your lists saved: ")
        db['directoryPath'] = directoryPath

    db.close()

def main():
    directoryConfig()                        #Här får användaren välja var filerna ska sparas
    db = shelve.open("ToDoListConfig")
    folderPath = db["directoryPath"]
    db.close()

    while not os.path.isdir(folderPath):                                                 #En while-loop som ser till att programmet inte kraschar när katalogen inte hittas
        folderPath = input("The directory could not be found. Please enter again: ")

    txtFiles = getTxtFilesInFolder(folderPath)

    print("Welcome to your to-do list! Select an existing to-do list below or create a new one:")   #Här visar den existerande filer

    for txtFile in txtFiles:
        print(txtFile[:-4])

    fileName = input("Please enter the name of the file you want to edit or create: ")   #Här får användaren välja vilken fil den vill öppna eller skapa
    filePath = getFilePath(folderPath, fileName)

    file = createOrOpenFile(filePath, createFile=True)
    if file is None:
        print("Could not locate or create file. Exiting.")
        return

    tasks = readTasksFromFile(filePath)        #Här visar den filerna i enumerate-läge vilket innebär att den inte kan ändras
    print("Your current to-do list:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task.strip()}")

    while True:                 #Här är en while-loop som körs när filerna väl är öppna. Då kan man lägga till, ta bort, byta lista och gå ur programmet.
        command = input("Enter 'add' to add a task, 'remove' to remove a task,'new' to choose another list or 'exit' to exit: ")
        if command.lower() == "exit": #Här kan användaren gå ut ur programmet
            break
        elif command.lower() == "add": #Här kan användaren lägga till saker till listan
            task = input("Please enter your task: ")
            file.write(task + "\n")
            print("Task added to the file.")
        elif command.lower() == "remove": #Här kan användaren ta bort saker från listan
            tasks = readTasksFromFile(filePath)
            print("Your current to-do list:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task.strip()}")

            taskIndices = [i+1 for i in range(len(tasks))]
            print(f"Task indices: {taskIndices}")

            taskIndex = int(input(f"Please enter the index of the task you want to remove (1-{len(tasks)}): "))
            removeTask(filePath, taskIndex)
        elif command.lower() == "new":  #Här körs en kod som gör det möjligt för användaren att välja en ny lista
            txtFiles = getTxtFilesInFolder(folderPath)
            print("Existing to-do lists:")
            for txtFile in txtFiles:
                print(txtFile[:-4])
            newFileName = input("Please enter the name of the new file you want to edit or create: ")
            newFilePath = getFilePath(folderPath, newFileName)
            newFile = createOrOpenFile(newFilePath, createFile=True)
            if newFile is None:
                print("Could not locate or create file. Exiting.")
                return
            tasks = readTasksFromFile(newFilePath)
            print(f"Your current to-do list ({newFileName}):")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task.strip()}")
            filePath = newFilePath
            file = newFile
        else:
            print("Invalid command.")

    file.close()

main()