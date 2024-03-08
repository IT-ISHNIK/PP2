#Write a Python program to copy the contents of a file to another file
import shutil

with open("new.txt", 'w') as file:
    shutil.copy("check.txt", "new.txt")
    file.close()