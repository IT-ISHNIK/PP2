#Write a Python program to calculate the area of a trapezoid.
"""Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5"""
height = int(input("Input height of trapezoid: "))
base1 = int(input("Input value of first base: "))
base2 = int(input("Input value of second base: "))
meanvalue = (base1 + base2)/ 2
area = meanvalue * height
print("Area of trapezoid is: ", area)
