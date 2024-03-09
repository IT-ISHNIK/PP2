#Write a Python program to find sequences of lowercase letters joined with an underscore.
from re import *
with open('data.txt', 'r', encoding='utf-8') as txt:
    x = findall("[a-z]+_+[a-z]+", txt.read())
if x :
    print('yes we have a match')
else:
    print("No we dont have a match")
