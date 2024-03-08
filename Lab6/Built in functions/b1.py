#Write a Python program with builtin function to multiply all the numbers in a list
list = [int(i) for i in input("Enter numbers seperated by space:").split(' ')]
res = 1
for i in list:
    res*=i
print("Result of multiplication of all elements is list is: ", res)
