#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
from re import *
with open('data.txt','r',encoding='utf-8') as txt:
    x = sub(r'[ ,.]', ':',txt.read())
    print(x)