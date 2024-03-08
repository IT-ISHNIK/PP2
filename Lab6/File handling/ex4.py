#Write a Python program to count the number of lines in a text file.
with open("check.txt", 'r') as file:
    count = 0
    for i in file:
        count +=1
print("There is", count, "lines")
