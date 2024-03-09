#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
from re import *
with open('data.txt','r', encoding='utf-8') as txt:
    qwerty = "DSAAlajlgfksdagkj"
    x = findall(r'\b([A-Z]{1}|[А-Я]{1})([a-z]+|[а-я]+)\b',txt.read())
    #y = findall(r'\b[A-Z][a-z]+\b',qwerty)
    if x:
        print("Yes WE HAVE")
    else:
        print('no havent')