'''
Write a Python program that invoke square root function after specific milliseconds
Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858
'''
import time 
import math
number = int(input("Enter your number: "))
res = int(math.sqrt(number))
ms = int(input("Enter delay time: "))
MsToS = ms/1000
time.sleep(MsToS)
print("Sqrt of", number, 'after', ms, 'miliseconds is', res)
