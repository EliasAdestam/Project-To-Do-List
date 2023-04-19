import os

def getTxtFilesInFolder(folder_path):
    files = os.listdir(folder_path)
    return [f for f in files if f.endswith('.txt') and f != "directoryPath.txt"]

def getFilePath(folder_path, file_name):
    return os.path.join(folder_path, f"{file_name}.txt")

def readTasksFromFile(file_path):
    with open(file_path, "r") as f:
        tasks = f.readlines()
    return tasks

def createOrOpenFile(file_path, create_file=False):
    if os.path.exists(file_path):
        mode = "a"
    elif create_file:
        mode = "w"
    else:
        return None
    return open(file_path, mode)

def removeTask(file_path, task_index):
    tasks = readTasksFromFile(file_path)

    if task_index < 1 or task_index > len(tasks):
        print("Invalid task index.")
        return

    task = tasks.pop(task_index - 1)

    with open(file_path, "w") as f:
        f.writelines(tasks)

    print(f"Task '{task.strip()}' removed from the file.")

def main():
    folder_path = input("Enter the directory where you want your lists to be saved here: ")
    with open("directory_path.txt", "w") as f:
        f.write(folder_path)
    txt_files = getTxtFilesInFolder(folder_path)

    print("Welcome to your to-do list! Select an existing to-do list below or create a new one:")

    for txt_file in txt_files:
        print(txt_file[:-4])

    file_name = input("Please enter the name of the file you want to edit or create: ")
    file_path = getFilePath(folder_path, file_name)

    file = createOrOpenFile(file_path, create_file=True)
    if file is None:
        print("Could not locate or create file. Exiting.")
        return

    tasks = readTasksFromFile(file_path)
    print("Your current to-do list:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task.strip()}")

    while True:
        command = input("Enter 'add' to add a task, 'remove' to remove a task, or 'exit' to exit: ")
        if command.lower() == "exit":
            break
        elif command.lower() == "add":
            task = input("Please enter your task: ")
            file.write(task + "\n")
            print("Task added to the file.")
        elif command.lower() == "remove":
            tasks = readTasksFromFile(file_path)
            print("Your current to-do list:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task.strip()}")

            task_indices = [i+1 for i in range(len(tasks))]
            print(f"Task indices: {task_indices}")

            task_index = int(input(f"Please enter the index of the task you want to remove (1-{len(tasks)}): "))
            removeTask(file_path, task_index)
        else:
            print("Invalid command.")

    file.close()

main()