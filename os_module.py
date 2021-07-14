import os

print(os.getcwd()) # gets the current working directory

# os.chdir('/Users/evanpavone/Desktop')  changes directory to desktop

print(os.listdir()) # lists contents of directory

if "myfolder" not in os.listdir():
    os.mkdir("myfolder") # creates a folder in current directory

try:
    os.makedirs("LearningPython/MadeDir/MadeAnotherDir")
except FileExistsError:
    print("Files already exists")

# delete specific directory
try:
    os.rmdir("LearningPython/MadeDir/MadeAnotherDir")
except OSError:
    print("Directory Not Empty... Deleting contents in directory")
except FileNotFoundError:
    print("Directory does not exist")
except:
    os.remove("LearningPython/MadeDir/MadeAnotherDir/random_file.py")
finally:
    try:
        print("Removing Directory")
        os.rmdir("LearningPython/MadeDir/MadeAnotherDir")
    except FileNotFoundError:
        print("File/Directory does not exist, creating one now")
        os.makedirs("LearningPython/MadeDir/MadeAnotherDir")
    finally:
        print("File/Directory created")