1.To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
2.Open the file "demofile2.txt" and append content to the file:
f = open("demofile2.txt", "a")
f.write("Now the file has more content!") #append text to last row
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

3.Open the file "demofile3.txt" and overwrite the content:

f = open("demofile3.txt", "w") 
f.write("Woops! I have deleted the content!")#delete all
f.close()
# close() method to free up system resources and ensure that any buffered data is written to the file.To save written

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())
