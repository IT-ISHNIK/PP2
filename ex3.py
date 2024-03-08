import os
#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
path = input("Enter path: ")
try:
    os.access(path, os.F_OK)
except:
    print("Happened a problem while running")
    quit()
if os.path.exists(path):
    directory = os.path.split(path)
    filename = os.path.split(path)
    print("Directory is:", directory, "Filename is", filename )
else:
    print("There is no such file")

