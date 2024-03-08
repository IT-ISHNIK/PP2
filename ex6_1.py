#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import os
file_names = [f"{chr(65+i)}.txt" for i in range (26)]
# for i in file_names:
#     with open(i,'w') as file:
#         pass
for i in file_names:
    os.remove(i)