#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
string = input('Enter the string: ')
upper = 0
lower = 0
for i in string:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print("Number of lower cases is -", lower, "Number of upper cases is -", upper)