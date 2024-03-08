#Write a Python program to list only all directories and files in a specified path.
from os import *
Path = input("Enter specified path: ")
try:
    for item in listdir(Path):
        item = path.join(Path, item)
        if path.isdir(item):
            print("Directory:", item)
        else:
            print("File:", item)
except FileNotFoundError:
        print("Specified path does not exist.")

print(listdir(Path))



