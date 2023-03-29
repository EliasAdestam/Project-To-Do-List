import os
print("Welcome to your to-do list! Select existing to-do list below or create a new one!")

file = open("Todolist_1.txt", "a")
file.write(input("Please enter your tasks here: "))
