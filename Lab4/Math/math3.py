#Write a Python program to calculate the area of regular polygon.
#Area = (number of sides × length of one side × apothem)/2
#Apothem = [(length of one side)/{2 ×(tan(180/number of sides))}].
from math import *
sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
angle = radians(180 / sides)
apothem = length/(2 * tan(angle))
area = (sides * length *apothem)/ 2
area = round(area,1)
print("Area of regualar polinom is:",area )

