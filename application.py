# 1. MY first program

print("Hello World")

# 2. Basics of Variables

# A Variable is a pointer to a given value
# A reserved memory location that stores a value
# Method (print) - prints the msg variable value
print('This is the next statement')
# Runs Line by line
# Variable is a container
number = 1997
# = is for assignment
print(number)
weight = 120

answer = number + weight
print(answer)

first_name = "Evan "
last_name = "Pavone"

sentence = first_name + last_name + " was born in " + str(number) + " and weighs " + str(weight) + " lbs"
name = first_name + last_name
# concatenation 
print(name)
print(sentence)
# str(number) converts the integer into a string

# 3. Basic Datatypes in Python

# Integer(number), String(Sentence), Boolean(True/False), Float(Decimal)
adult = True # boolean
data_type_int = type(12)
data_type_float = type(12.9)
data_type_str = type("Hello World")
data_type_boolean = type(adult)
data_type_from_variable = type(number)
print(data_type_int)
# -> <class 'int'> -> Saying that 12 is an integer
print(data_type_float)
# -> <class 'float'>
print(data_type_str)
# -> <class 'str'>
print(data_type_boolean)
# -> <class 'bool'>
print(data_type_from_variable)
# -> <class 'int'>

# 4. Basic Arithmetic in Python

# Basic math - does anything inside ( ) first - multiplication * - division / - addition + - subtraction -

num1 = 3
num2 = 10

answer = num2%num1 # % modulus operator

print(answer)