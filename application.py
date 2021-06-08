# 1. MY first program

print("Hello World")

# 2. Basics of Variables

# A Variable is a pointer to a given value
# A reserved memory location that stores a value
# Function (print) - prints the msg variable value
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

# 5. Indexing and Slicing Strings

new_sentence = "this is a sentence"
alphabet = "abcdefghijklmnopqrstuvwxyz"

# /n = new line
# index's of the sentence t-0 h-1 i-2 s-3 ' '-4 i-5 s-6 ' '-7 a-8 ' '-9 s-10 e-11 n-12 t-13 e-14 n-15 c-16 e-17

print(new_sentence[0]) # the first index of new_sentence is t with an index of 0
# first character will always be 0
print(new_sentence[-1]) # -1 will give me the last character in the string

print(new_sentence[0:4]) # will grab a word from the sentence - s is index 3 but it is non inclusive so need to go one step further and put 4

# ON MY OWN - grab the word "is" from new_sentence

print(new_sentence[5:7]) # = is
print(new_sentence[8]) # = a
print(new_sentence[10:18]) # = sentence
print(alphabet[3:]) # defg... gets the starting position and goes to the end because I didn't give an end position
# This is known as slicing

# Getting every other character of the alphabet

print(alphabet[0:26:2])

# 6. Basic String Methods

string_sentence = "this is a sentence that is a string." #performs first

string_sentence = string_sentence.upper() # upper method - performs second

print(string_sentence) #performs third

string_sentence = "this is a sentence that is a string."

print(string_sentence.upper()) # this will also work
print(string_sentence.capitalize()) # Capitalize the first character and lowercases everything else
print(string_sentence.isdigit()) # Boolean - if the characters are not numbers it will return false.
print(string_sentence.isalnum()) # letters and numbers - will return false because of spaces
print(string_sentence.startswith("this"))

# 7. Formatting Strings Using the Format Method

sentence = "The sum of 5 + 10 is {0}".format(50) # you can pass anything. -> The sum of 5+10 is 50 -> The sum of 5+10 is happy day
print(sentence)

sentence = "The sum of {0} + {1} is {2}".format(10, 15, 25)
print(sentence)