#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
from re import *
with open("data.txt", "r", encoding="utf-8") as txt:
    x = findall('ab|abb', txt.read())
    if x:
        print("Yes we have match")
    else:
        print("no we dont have mathces")