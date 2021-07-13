my_file = None

try:
    my_file = open('/Users/evanpavone/Documents/Coding/Python/LearningPython/fileIO-example/sample.txt', mode="r")
    print(my_file.read())
except IOError:
    """
    There are different types of exception errors. TypeError, FileNotFoundError etc...
    You can capture specific errors
    """
    print("Issue with working with the file...")
except:
    # general catch all error
    print("Error occurred, logging to the system")
finally:
    if my_file != None:
        my_file.close()
    print("This will always run regardless of whether we have an exception or not")

print("This line was run...")