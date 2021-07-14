import os

for dirpath, dirnames, filenames in os.walk("/Users/evanpavone/Documents/Coding/Python/LearningPython/myfolder"):
    #unpacking
    # print(dirpath)
    # print(dirnames)
    # print(filenames)
    # print(" ------------ ")
    pass
    
"""
/Users/evanpavone/Documents/Coding/Python/LearningPython/myfolder - dirpath
['stuff'] - dirnames
['sample.txt'] - filenames
 ------------ 
/Users/evanpavone/Documents/Coding/Python/LearningPython/myfolder/stuff - dirpath
['data'] - dirnames
['sample.txt'] - filenames
 ------------ 
/Users/evanpavone/Documents/Coding/Python/LearningPython/myfolder/stuff/data - dirpath
[] - dirnames - means no directory
['peacock.jpeg'] - filenames
 ------------ 
"""

# os.environ.get("HOME") + "/" + "myfile.txt" /Users/evanpavone/myfile.txt

print(os.path.join(os.environ.get("HOME"), "myfile.txt")) # /Users/evanpavone/myfile.txt

print(os.path.basename("/bin/tools/myfile.txt")) # myfile.txt - used to get basename... thats the file at the directory location given

print(os.path.dirname("/bin/tools/myfile.txt")) # /bin/tools - get the directory name only, not the file

print(os.path.split("/bin/tools/myfile.txt")) # ('/bin/tools', 'myfile.txt') - will give directory name and basename in a tuple 

print(os.path.exists("/bin/tools/myfile.txt")) # False - used to check if the path exists on the computer

print(os.path.isfile("/bin/tools/myfile.txt")) # used to check if file exists in the specified path

print(os.path.isdir("/bin/tools/myfile.txt")) # check if directory exists in the specified path

print(os.path.splitext("/bin/tools/myfile.txt")) # ('/bin/tools/myfile', '.txt') - get file with path and file extension in a tuple