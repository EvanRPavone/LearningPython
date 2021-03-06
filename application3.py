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

# 2. *args and **kwargs in Python

def mysum(*args): # to have an unlimited number of arguments put *args in () instead
    return sum(args)

result = mysum(10,20,30,1,1,1,1,10,5,6)   

print(result)

def key_value_func(**kwargs):
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs.get("weight"))
    print(kwargs.get("name"))
    print(kwargs.get("age"))
    print(kwargs.get("address")) # no value assigned to the key address - will return
    
key_value_func(name="mike", weight=200, age=27)

# 3. Basics of Variable Scope

age = 23 # Global Scope

print(age)

def increase_age():
    age = 30 # local scope
    
increase_age() # age is local to this function only
    
print(age) # 23 Global Scope

# 4. Scope and Nested Functions

def increase_age_again():
    age = 30
    
    # defining a nested function
    def add_4_to_age(age):
        age = age + 4
        print("NESTED METHOD: " + str(age))
        
    # calling the nested function
    add_4_to_age(age)
    print(age) # will print 30 not 34 - outside of the scope of add_4 - in the scope of increase_age_again
        
increase_age_again()