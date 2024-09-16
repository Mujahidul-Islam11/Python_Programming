"""write a python program to print the contents of a directory 
   by using built-in module os"""

import os

directory_path = "/"

contents = os.listdir(directory_path)

for item in contents:
    print(item)
