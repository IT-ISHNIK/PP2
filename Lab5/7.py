#Write a python program to convert snake case string to camel case string.
from re import *
with open('data.txt','r',encoding='utf-8') as txt:
    text = txt.read()
    y = findall('[a-zA-Z]+_[a-zA-Z]+',txt.read())
def change(list, iter):
    newlist = []
    for i in list:
        value = "".join(i.capitalize() for i in list.split('_'))
        newlist.append(value)
    return(newlist[iter])
z = ""
for i in range(0, len(y)):
    x = sub('[[a-zA-Z]+_[a-zA-Z]+]',change(i))
    z = x
print(z)