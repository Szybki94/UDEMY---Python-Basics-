import os
import time

dir = input("Please select path to directory:\t")


if os.path.isdir(dir):
    print("Directory exist")
    file = input("Please select file name:\t")
    path = os.path.join(dir, file)
    if not  os.path.isfile(path):
        print(path, "File does not exist")
    else:
        print()
        print("-"*60)
        print("File properties".center(60))
        print("Last modified date:\t", time.localtime(os.path.getmtime(path)))
        print("Size in bytes:\t\t", os.path.getsize(path))
        print("Current directory is:\t\t", os.getcwd())
        print("Relative path to the file is", os.path.relpath(path))
              
        

else:
    print("NOT OK")
    
