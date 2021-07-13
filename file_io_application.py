myfile = open('/Users/evanpavone/Documents/Coding/Python/LearningPython/fileIO-example/sample.txt') # cant have this file be opened more than once

content = myfile.read() # reads the contents of sample.txt from beginning to end
print(content)

myfile.seek(0) # will put the cursor at the beginning of the file. resets the cursor

print("---------------")
data = myfile.read() # will not read if printed. The read function takes the cursor from the beginning all the way to the end. so when the content variable is printed the cursor is at the end and will not go back.
print(data)

myfile.seek(0) # will put the cursor at the beginning of the file. resets the cursor

print("---------------")

content_list = myfile.readlines() # to read each line there is a readlines method. each line in the file will be saved in its own element in the list

myfile.close()#will close the file

print(content_list)
"""
['It involves drastically reducing carbohydrate intake and replacing it with fat. This reduction in carbs puts your body into a metabolic state called\xa0ketosis.\n', '\n', 'When this happens, your body becomes incredibly efficient at burning fat for energy.\n', 'It also turns fat into ketones in the liver, which can supply energy for the brain.\n', '\n', 'Ketogenic diets can cause massive reductions in blood sugar and insulin levels. This, along with the increased ketones, has numerous health benefits.']
"""

with open('/Users/evanpavone/Documents/Coding/Python/LearningPython/fileIO-example/sample.txt', mode='a') as my_file:
    """
    This open syntax already opens and closes the file
    If I change the filename it will make a new file in that location if I use the write mode
    MODES:
    a = append - adds to the file
    w = write - overwrites the file. The data will be replaced
    r = read - cannot write to it. Read only mode
    r+ = read and write
    w+ = override the file completely and have the ability to read it
    """
    my_file.write("\nThis is my sentence") # appended to the end of the file
    
my_appended_file = open('/Users/evanpavone/Documents/Coding/Python/LearningPython/fileIO-example/sample.txt')
print(my_appended_file.read()) #will have This is my sentence at the end.
my_appended_file.close()