# write a python program to print the content of directory using 
# the os module. search online for the function which does that

import os

# Specify the directory path
directory_path = '.'
 # '.' represents the current directory

# Get the list of files and directories in the specified path
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
