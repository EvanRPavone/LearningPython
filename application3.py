# SECTION 3

# 1. Intro to Creating Functions

# function name - open and closed () - in () are arguments

# help(print)  gives us what the function is all about. gives a signature (template of how the function is used)

def greet_person(value = "your name"): # passing a parameter of value with a default value of your name
    '''
    DOCSTRING: This returns a greeting
    INPUT: value
    OUTPUT: Hello ... name
    '''
    print("Hello " + str(value) + ", this is the greet_person function")

greet_person() # calling the function
greet_person("Evan") # passing an argument
greet_person(23)

def remainder(x, y):
    '''
    DOCSTRING: This returns the remainder of x and y
    INPUT: x, y
    OUTPUT: The remainder of x and y
    '''
    return "The remainder of " + str(x) + " and " + str(y) + " is " + str(x%y)
    
answer = remainder(42, 15)
print(answer)
