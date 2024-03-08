1.To delete a file, you must import the OS module, and run its os.remove() function:

Remove the file "demofile.txt":

import os
os.remove("demofile.txt")
2.Check if File exist and then delete it:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
3.To delete an entire folder, use the os.rmdir() method:

Example
Remove the folder "myfolder":

import os
os.rmdir("myfolder")
4.If you want to delete non-empty directories as well, you would need to recursively delete the files and 
subdirectories within them before calling os.rmdir()