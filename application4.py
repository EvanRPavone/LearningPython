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