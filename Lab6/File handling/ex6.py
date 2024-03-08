#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
from string import *
import os
file_names = [f"{letter}.txt" for letter in ascii_uppercase]
for i in file_names:
    with open(i,"w") as file:
        pass
for i in file_names:
    os.remove(i)