import os

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

def main():
    folderPath = input("Enter the directory where you want your lists to be saved here: ")  #Här får användaren välja var filerna ska sparas
    with open("directoryPath.txt", "w") as f:
        f.write(folderPath)

    while not os.path.exists(folderPath):                                                 #En while-loop som ser till att programmet inte kraschar när katalogen inte hittas
      folderPath = input("The directory could not be found. Please enter again: ")

    txt_files = getTxtFilesInFolder(folderPath)

    print("Welcome to your to-do list! Select an existing to-do list below or create a new one:")   #Här visar den existerande filer

    for txt_file in txt_files:
        print(txt_file[:-4])

    fileName = input("Please enter the name of the file you want to edit or create: ")   #Här får användaren välja vilken fil den vill öppna eller skapa
    filePath = getFilePath(folderPath, fileName)

    file = createOrOpenFile(filePath, createFile=True)
    if file is None:
        print("Could not locate or create file. Exiting.")
        return

    tasks = readTasksFromFile(filePath)        #Här visar den filerna i enumerate-läge vilket innebär att den inte kan ändras för tillfället
    print("Your current to-do list:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task.strip()}")

    while True:                 #Här är en while-loop som körs när filerna väl är öppna. Då kan man lägga till, ta bort och gå ur programmet.
        command = input("Enter 'add' to add a task, 'remove' to remove a task, or 'exit' to exit: ")
        if command.lower() == "exit":
            break
        elif command.lower() == "add":
            task = input("Please enter your task: ")
            file.write(task + "\n")
            print("Task added to the file.")
        elif command.lower() == "remove":
            tasks = readTasksFromFile(filePath)
            print("Your current to-do list:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task.strip()}")

            taskIndices = [i+1 for i in range(len(tasks))]
            print(f"Task indices: {taskIndices}")

            taskIndex = int(input(f"Please enter the index of the task you want to remove (1-{len(tasks)}): "))
            removeTask(filePath, taskIndex)
        else:
            print("Invalid command.")

    file.close()

main()