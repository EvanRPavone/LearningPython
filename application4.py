# SECTION 4

# 1. Control Flow: If & Else Statements

elephant = 800
hippo = 900

if elephant < hippo:
    print("Elephant weighs less than the hippo")
else:
    print("hippo weighs less than the elephant") # <-----
    
if True:
    print("This will always be printed")
else:
    print("this will never be printed")
    
if (elephant < hippo and (3 > 2)):
    print("the if statement evaluated to true")
    if 5 < 7:
        print("5 < 7")
else:
    print("if statement evaluated to false")
    
# MESSING AROUND

my_list = ["Evan", "Robert", "Pavone"]

if "Evan" in my_list or "Robert" in my_list or "Pavone" in my_list or "Bobby" in my_list:
    print("Evan, Robert and Pavone are on the List")
    if "Bobby" in my_list:
        print("Bobby is also on the list")
    else:
        print("Bobby is not on the list")
else:
    print("These people are not on the list")
    
# 2. Control Flow: Elif statements

# if something takes place do this, if something else takes place do that, if something else takes place do that etc..

animal = "ape"

if animal == "cow":
    print("eats grass")
elif animal == "bird":
    print("eats seeds")
elif animal == "monkey" or animal == "ape":
    print("eats bananas")
else:
    print("We don't know what the animal eats")

# 3. For Loops

# Running a code over, over, and over again

farm_animals = ["goat", "horse", "chicken", "cow", "dog"]

for animal in farm_animals:
    print(animal)
    """
    This will print:
    goat
    horse
    chicken
    cow
    dog
    """
    sentence = animal + " is safe in our farm"
    print(sentence)
    """
    goat is safe in our farm
    horse is safe in our farm
    chicken is safe in our farm
    cow is safe in our farm
    dog is safe in our farm
    
    NOTE: Will not actually print like this... it will print goat then goat is safe in our farm, horse then horse is safe in our farm etc...
    """
    
touple_of_names = ('Evan', 'Rob', 'Jerry', 'Kevin', 'Griffin', 'Bryce')
counter = 0

for name in touple_of_names:
    if "Bryce" in name:
        print("Bryce is not allowed inside")
        continue
    counter = counter + 1
    sentence = str(counter) + ". " + name + " is allowed inside."
    print(sentence)
    """
    Evan is allowed inside
    Rob is allowed inside
    Jerry is allowed inside
    Kevin is allowed inside
    Griffin is allowed inside
    Bryce is not allowed inside
    
    TO TRY: have 1,2,3 before each sentence (counter)
    """
    
greeting = "hello my name is Evan"

for char in greeting:
    if char == "n":
        continue # will skip the letter n
    print(char)
    
print("Loop is terminated by this point")

# 4. Pass Statement in For Loops

my_objects = ['computer', 'car', 'bottle', 'tv']

for object in my_objects:
    # python expects some type of instruction, cant be left empty
    pass # Placeholder. does nothing except keeps the structure. Ex. telling a coder to come to this next week and finish it but keeps the code running

print("pass statement used here")
# for loops doesn't need to have a variable, it can use a list, string, touple, etc.. too.

for object in ['computer', 'car', 'bottle', 'tv']:
    print(object)
    
# 5. While Loops

# while something is true, do something
# while <condition is true>:
#   # do something
# else
#   # do something else...

x = 0

while x < 10:
    print(x)
    # x = x + 1 is the same as below
    x += 3 # add whatever number on the right.. as soon as it hits 10 it will print the else
    
    if(x == 6):
        continue # will not skip 6 because we are printing before this happens
    
else:
    print("x is not less than 10")
    
# 6. Looping and Unpacking with Dictionaries and Touples

# Dictionary

employees = {'mike': 27000, 'john': 65000, 'rebecca': 60000, 'tom': 100000}

for person in employees:
    print(person) # by default the key will be printed. The employee names

for entry in employees.items():
    print(entry) # will get all the salaries for each employee. returns a bunch of touples which returns the key value pair
    
for salary in employees.values():
    print(salary) # will return only the salary which are the values
    
for employee, salary in employees.items(): # this is known as unpacking
    print(employee)
    print(salary)
    """
    mike
    27000
    john
    65000
    rebecca
    60000
    tom
    100000
    """

employee_touple = [('mike', 27000, 29), ('john', 65000, 47), ('rebecca', 60000, 62), ('tom', 100000, 29)]

for (employee, salary, age) in employee_touple:
    print(employee + " gets paid $" + str(salary) + " a year" + " and is " + str(age) + " years old")
    """
    mike gets paid $27000 a year and is 29 years old
    john gets paid $65000 a year and is 47 years old
    rebecca gets paid $60000 a year and is 62 years old
    tom gets paid $100000 a year and is 29 years old
    """

