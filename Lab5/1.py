#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
from re import *
with open('data.txt', 'r', encoding="utf-8") as txt:
    x = findall(r'ab*', txt.read())
    if x:
        print("Yes, we have a match" )
        print(x)
    else:
        print("No, we have no match")
