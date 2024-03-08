#Python has several functions for creating, reading, updating, and deleting files.

1.
The open() function takes two parameters; filename, and mode.
2.
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
3.
There is 2 mods
"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
4.FUnctions 
You can return one line by using the readline() method
#Read two lines of the file:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
5.Loop through the file line by line:

f = open("demofile.txt", "r")
for x in f:
  print(x) #Combiantion of lines
6.Close the file when you are finish with it:

f = open("demofile.txt", "r")
print(f.readline())
f.close()