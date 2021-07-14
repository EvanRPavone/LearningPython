import sys
import re

"""
IN TERMINAL:

If i were to run a program in the terminal and pass arguments too I would need to have sys imported and the indexes specified

python3 <filename>.py <arg1> <arg2>

<filename> = [0]
<arg1> = [1]
<arg2> = [2]
"""
print(sys.argv[0]) # argv_command_line.py
print(sys.argv[1]) # Evan
print(sys.argv[2]) # 23
print(sys.argv[1:]) # Can have unlimited number of arguments

argument_list = sys.argv[1:]

for arg in argument_list:
    print(arg)
    """
    python3 argv_command_line.py Evan 23 25 Gamer Yikers
    Evan
    23
    25
    Gamer
    Yikers
    """
    
# w3schools.com/python/python_regex.asp
# must import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
y = re.search("^The.*Spain$", txt)
print(x)
print(y)

if (y):
    print("YES! We have a match!")
else:
    print("No Match")