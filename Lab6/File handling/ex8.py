#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

path = input("Enter specified path: ")
#1
if (os.path.exists(path)):
    print("Yes this path exists")
else:
    print("No there is no such file")
#2
print("Existence of a specified path:",os.access(path, os.F_OK))
print("Readability:", os.access(path, os.R_OK))
print("Writability:", os.access(path, os.W_OK))
print("Executablness:", os.access(path, os.X_OK))
#3
os.remove(path)