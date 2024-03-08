# \n - new line(1 char)    "rasul\n hello"
1. rstrip('!') - remove all same character at the end off the string
2. string = "hello world!!!!!!!" - - - - - > string.rstrip('!') - - - - > hello world
rstrip() - - - > delete new line
3. startwith() - is a string method that checks whether a string starts with a specified prefix.
4.  if not line.startswith('From: ') # not would transfer to above into "if  line do not start with ... "
        continue
    print line
5.In to select line
for line in txt:
    line = line.rstrip()
    if not 'rasul agatai' in line :
        continue
    print(line)
same as 
    if 'rasul agatai' in line :
        print(line)
6.Prompt for file name
fname = input("Input file name")
file = open(fname)
#Bad file name - file with spaces, not every OS can recognize it
7.
fname = input("Input file name: ")
try:
    file = open(fname)
except:
    print("File cant be open, please cheack it")
    quit()
If it is ok we countinue our code
    #quit() is a built-in function in Python that raises the SystemExit exception, it exits the interactive Python session . 
there is errors which can take place with except like:
except  FileNotFoundError#: Raised when a file or directory is requested but cannot be found.
        IOError#: Raised when an input/output operation (such as opening or reading a file) fails.
        TypeError#: Raised when an operation or function is applied to an object of inappropriate type.
8. OS module
 access()
 fwalk()
 listdir()
9. SHUTIL module
 copy()
10.import TIME
delay()
