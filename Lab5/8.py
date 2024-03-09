#Write a Python program to insert spaces between words starting with capital letters.
import re

with open("row.txt" , 'r', encoding = "utf-8") as f:
    text = f.read()

def transfer(text):
    words = re.findall(r'\b[A-ZА-Я]\w+\b', text) 
    for word in words:
        print(word,end = " ")
transfer(text)
