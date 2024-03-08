#Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
"""
F_OK: Tests existence of the path.
R_OK: Tests readability of the path.
W_OK: Tests writability of the path.
X_OK: Checks if path can be executed.
"""
from os import *

path = input("Enter specified path: ")

print("Existence of a specified path:",access(path, F_OK))
print("Readability:", access(path, R_OK))
print("Writability:", access(path, W_OK))
print("Executablness:", access(path, X_OK))




