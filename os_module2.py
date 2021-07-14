import os

for dirpath, dirnames, filenames in os.walk("/Users/evanpavone/Documents/Coding/Python/LearningPython/myfolder"):
    #unpacking
    print(dirpath)
    print(dirnames)
    print(filenames)
    print(" ------------ ")
    
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