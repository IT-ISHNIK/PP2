#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
from re import *
with open('data.txt','r',encoding='utf-8') as txt:
    x = findall(r'^a.*b$',txt.read())
    if x:
        print('Yes we have a match')
    else:
        print("We dont have a match")


